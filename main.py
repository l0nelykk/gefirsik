import os

from config import get_api_key
from logger import log_event, get_log_file
from gemini_client import ask_gemini
from commands import handle_user_input

print("gefirsik started. Type 'exit' to quit.")

while True:

    with open('gcode.py', 'w', encoding='utf-8') as f:
        f.write('#python')

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

    with open('gcode.py', 'w', encoding='utf-8') as f:
        f.write(final_response)
    
    print(f"gefirsik: {final_response}")
    os.system("cat gcode.py")
    print("continue?")
    
    sudo_opsec = input()
    if sudo_opsec == 'n':
        continue

    exec(open('gcode.py').read())
    os.system('python gcode.py')
