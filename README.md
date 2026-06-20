​gefirsik
​An Android assistant powered by the Gemini API that executes basic functions such as opening apps, capturing screenshots, and handling messaging based on structured JSON commands.
​Prerequisites
​Python 3+
​Python dependencies: requests, python-dotenv
​Google AI API key
​Setup
​Install the required Python packages:
pip install requests python-dotenv
​Create a .env file in the root directory and add your API key:
GEMINI_API_KEY="your_api_key_here"
​Run the application:
python main.py
​Usage
​Type your request in the console. If it relates to phone control, the assistant processes it via JSON actions.
​Type 'logs' to view the session log.
​Type 'exit' or 'quit' to stop the assistant
