# chatbot.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def ask_mistral_chat(messages: list, model="mistral-small"):
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise Exception("MISTRAL_API_KEY not found in environment variables.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers=headers,
        json={
            "model": model,
            "messages": messages
        }
    )

    if response.status_code != 200:
        raise Exception(f"Mistral API Error: {response.status_code} - {response.text}")

    return response.json()["choices"][0]["message"]["content"]
