# main.py
import streamlit as st
from generator import generate_questions
from fpdf import FPDF
from io import BytesIO
import fitz  # PyMuPDF

# ============ Utility Functions ============

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    return "".join([page.get_text() for page in doc])

def generate_pdf(questions: list[str]) -> BytesIO:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_title("AI Interview Questions")

    pdf.set_text_color(0, 0, 128)
    pdf.cell(0, 10, "AI-Generated Interview Questions", ln=True, align='C')
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)

    for idx, question in enumerate(questions, start=1):
        pdf.multi_cell(0, 10, f"{idx}. {question.strip()}", align='L')
        pdf.ln(1)

    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    pdf_stream = BytesIO()
    pdf_stream.write(pdf_bytes)
    pdf_stream.seek(0)
    return pdf_stream

# ============ Page Configuration ============

st.set_page_config(
    page_title="Smart Interview Question Generator",
    page_icon="🎯",
    layout="centered"
)

# ============ Sidebar ============

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712100.png", width=100)
    st.markdown("## 🤖 AI QuestionGen")
    st.markdown(
        "<p style='font-size: 14px;'>Instantly generate technical interview questions using your resume.</p>",
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.info("📄 Upload your resume (PDF) or paste it manually.")
    st.markdown("<small>Made with ❤️ by <strong>Vikas Ahirwar</strong></small>", unsafe_allow_html=True)

# ============ Header ============

st.markdown("<h1 style='text-align: center; color: #3366cc;'>🚀 Smart Interview Question Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px;'>Generate job-ready questions tailored to your skills and experience!</p>", unsafe_allow_html=True)
with st.expander("💡 How to Use This App", expanded=False):
    st.markdown("""
    - **Upload your resume** as a PDF *or* paste your resume text manually.
    - The app uses **AI** to generate 5–10 technical interview questions.
    - You can **download** the questions as a clean PDF.
    - Make sure your resume is detailed with technical skills/projects for better results.
    """)

st.markdown("### 📥 Resume Input")

# ============ Input Area ============

col1, col2 = st.columns(2)

with col1:
    uploaded_pdf = st.file_uploader("📤 Upload Resume (PDF)", type=["pdf"])

with col2:
    resume_text = st.text_area(
        "📝 Or Paste Resume Text",
        height=220,
        placeholder="Paste your full resume text here..."
    )

# ============ Process Text ============

final_text = ""
if uploaded_pdf:
    final_text = extract_text_from_pdf(uploaded_pdf)
elif resume_text.strip():
    final_text = resume_text.strip()

# ============ Generate Questions Button ============

st.markdown("### 🎯 Generate Questions")

if st.button("✨ Generate Interview Questions", use_container_width=True):
    if not final_text:
        st.warning("⚠️ Please upload or paste your resume first.")
    else:
        with st.spinner("🧠 Analyzing your resume..."):
            try:
                response = generate_questions(final_text)
                questions_list = [q.strip() for q in response.split("\n") if q.strip()]

                if questions_list:
                    st.success("✅ Questions Generated Successfully!")
                    st.markdown("### 📋 Questions Preview")

                    with st.expander("Click to Expand", expanded=True):
                        for idx, q in enumerate(questions_list, 1):
                            st.markdown(f"**{idx}.** {q}")

                    st.markdown("### 📎 Download as PDF")
                    pdf_file = generate_pdf(questions_list)

                    st.download_button(
                        label="📄 Download Questions PDF",
                        data=pdf_file,
                        file_name="interview_questions.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
                else:
                    st.warning("⚠️ No questions were generated. Try a different resume.")

            except Exception as e:
                st.error(f"❌ Error: `{e}`")

# ============ Footer ============

st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>🔒 All processing is done locally. No data is stored.</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>✨ Built with 💙 by <b>Vikas Ahirwar</b> | Powered by <b>Mistral AI</b></div>",
    unsafe_allow_html=True
)
