import json
import subprocess

def open_app(app_name):
    try:
        subprocess.run(["am", "start", "-n", app_name], check=True)
        return f"Opened {app_name}"
    except Exception as e:
        return f"Failed to open {app_name}: {e}"

def send_message(contact, text):
    return f"Sending '{text}' to {contact}"

def take_screenshot():
    return "Screenshot taken (placeholder)"

def execute_command_from_json(json_str):
    try:
        data = json.loads(json_str)
        action = data.get("action")
        params = data.get("params", {})
        message = data.get("message", "")

        if action == "open_app":
            app = params.get("app_name")
            if app:
                result = open_app(app)
                return f"{message}\n{result}"
            return "Error: app_name missing"

        elif action == "send_message":
            contact = params.get("contact")
            text = params.get("text")
            if contact and text:
                result = send_message(contact, text)
                return f"{message}\n{result}"
            return "Error: contact or text missing"

        elif action == "take_screenshot":
            result = take_screenshot()
            return f"{message}\n{result}"

        else:
            return f"Unknown action: {action}"

    except json.JSONDecodeError:
        return None

def handle_user_input(user_input, gemini_response):
    result = execute_command_from_json(gemini_response)
    if result:
        return result
    return gemini_response
