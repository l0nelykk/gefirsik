from config import get_api_key
from logger import log_event, get_log_file
from gemini_client import ask_gemini
from commands import handle_user_input

print("gefirsik started. Type 'exit' to quit.")

while True:
    user_input = input("> ")

    if user_input.lower() in ["exit", "quit"]:
        log_event("Assistant stopped by user")
        print("Goodbye.")
        break

    if user_input.lower() == "logs":
        print("\n--- Logs ---\n")
        print(get_log_file())
        continue

    gemini_response = ask_gemini(user_input)
    final_response = handle_user_input(user_input, gemini_response)
    print(f"gefirsik: {final_response}")
