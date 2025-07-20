import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

def generate_questions(resume_text, difficulty="Medium", category="General", count=5):
    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        raise Exception("MISTRAL_API_KEY not found in environment variables.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are a technical HR interviewer. Based on the following resume, generate {count} {difficulty}-level technical interview questions relevant to the candidate’s experience, projects, and skills in the domain of {category}. Ensure the questions are smart, concise, and contextual to their resume.

Resume:
\"\"\" 
{resume_text}
\"\"\"
"""

    data = {
        "model": "mistral-small",  # Options: mistral-small, mistral-medium, mistral-large
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code != 200:
        raise Exception(f"Mistral API Error: {response.status_code} - {response.text}")

    result = response.json()
    return result["choices"][0]["message"]["content"]
