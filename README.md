# 🤖 Smart InterviewQAI

**Smart InterviewQAI** is a Streamlit-based app that uses **Mistral AI** to automatically generate **technical interview questions** based on your resume. Just upload a PDF or paste your resume, and let the AI do the rest!

---

## 🚀 Features

- 📤 Upload your resume (PDF) or paste the text
- 🎯 AI analyzes your resume using Mistral AI API
- ✅ Generates 8–12 technical interview questions
- 📄 Download questions as a neatly formatted PDF
- 🔐 Secure API key handling using Streamlit secrets

---

## 🖼️ Demo Screenshot

![Smart InterviewQAI Demo](https://cdn-icons-png.flaticon.com/512/4712/4712100.png)

---

## 🌐 Live App

👉 [Click here to try the app](https://smart-ai-interviewq.streamlit.app/)

---

## 🛠️ Tech Stack

| Technology    | Usage                          |
|---------------|---------------------------------|
| Python        | Backend logic                  |
| Streamlit     | Web UI                         |
| MistralAI     | AI interview question generator |
| FPDF          | PDF export of questions         |
| PyMuPDF       | Extract text from PDF resumes   |

---

## 📦 Installation (Run Locally)

```bash
git clone https://github.com/v4viki/smart-interviewQAI.git
cd smart-interviewQAI
pip install -r requirements.txt
