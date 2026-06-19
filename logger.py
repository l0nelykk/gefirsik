import datetime
import os
from config import LOG_FILE

def log_event(message, level="INFO"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [{level}] {message}\n")

def get_log_file():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "No logs yet."
