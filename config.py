import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
LOG_FILE = "logs/gefirsik.log"
PROMPT_FILE = "prompt2.txt"

def get_api_key():
    if not API_KEY:
        raise ValueError("API key not found in .env file")
    return API_KEY

def get_prompt():
    try:
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "You are gefirsik, a phone assistant."
