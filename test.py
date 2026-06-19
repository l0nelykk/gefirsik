import requests
import json
from dotenv import load_dotenv
import os


class client:
    pass


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("API_KEY is not found")

model_name = "gemini-3.5-flash"  # или "gemini-2.5-flash" (если 3.5 не пустит бесплатно)

url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={API_KEY}"

usr_input = input('input message: ')

payload = {
    "contents": [
        {
            "parts": [
                {"text": usr_input}
            ]
        }
    ]
}

response = requests.post(url, json=payload)
print(response.status_code)

if (response.status_code == 200):
    print(response.json()['candidates'][0]['content']['parts'][0]['text'])

else:
    print(f"Error: {response.status_code}")
    print(response.text)

    
