import requests
import json
from config import get_api_key, get_prompt
from logger import log_event

API_KEY = get_api_key()
model_name = "gemini-2.5-flash"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={API_KEY}"

def ask_gemini(user_input):
    system_prompt = get_prompt()
    log_event(f"User: {user_input}")

    payload = {
            "contents": [
                {
                    "parts": [
                        {"text": user_input}
                    ]
                }
            ],
            "systemInstruction": {
                "parts": [
                    {"text": system_prompt}
                ]
            }
        }

    try:
        response = requests.post(url, json=payload, timeout=30)
        if response.status_code == 200:
            data = response.json()
            answer = data['candidates'][0]['content']['parts'][0]['text']
            log_event(f"Response: {answer}")
            return answer
        else:
            error_text = f"API Error: {response.status_code} - {response.text}"
            log_event(error_text, "ERROR")
            return f"API Error: {error_text}"
    except Exception as e:
        log_event(f"Exception: {e}", "ERROR")
        return f"Error: {e}"
