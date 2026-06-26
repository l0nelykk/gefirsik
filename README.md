################################################################################
#                                                                              #
#   ▄████████ ████████▄   ▄█   ▄█          ▄████████ ██▄▄▄▄   ███    █▄       #
#  ███    ███ ███   ▀███ ███  ███         ███    ███ ███▀▀███ ███    ███      #
#  ███    █▀  ███    ███ ███▌ ███         ███    ███ ███   ███ ███    ███      #
#  ███        ███    ███ ███▌ ███        ▄███▄▄▄▄██▀ ███   ███ ███    ███      #
# ▀███████████ ███    ███ ███▌ ███       ▀▀███▀▀▀▀▀   ███   ███ ███    ███      #
#          ███ ███    ███ ███  ███         ███    ███ ███   ███ ███    ███      #
#    ▄█    ███ ███   ▄███ ███  ███▌    ▄   ███    ███ ███   ███ ███    ███      #
#  ▄████████▀  ████████▀  █▀   █████▄▄██   ██████████  ▀█   █▀  ████████▀       #
#                                ▀                                              #
#                                                                              #
#                        your pocket code-writing assistant                     #
#                                                                              #
################################################################################

what is gefirsik

it's a termux assistant that doesn't just follow commands - it writes its own python code on the fly. you tell it what you want, gemini generates code, and it runs right there on your phone.

no predefined functions. no hardcoded actions. just pure generated code doing whatever you ask.

how it works

you type something -> gemini gets it -> writes python code -> executes it in termux

that's it. if you need to open an app, it'll write the code. need to send an sms? it'll figure out the intent. want to scrape a website, turn on the torch, read a file, post to an api? it'll generate code for that too.

whatever you can do in termux with python, gefirsik can try to do it for you.

========================================

why two prompts

prompt.txt - old one. used when the assistant had a fixed set of functions (open_app, send_message, etc). kept for reference but not really used anymore.

prompt2.txt - the real one. this tells gemini to generate python code. no json, no predefined actions - just raw executable code.

========================================

requirements

- android with termux
- python 3+
- gemini api key (from google ai studio)
- common sense (you're about to run ai-generated code on your phone)

========================================

quick setup

pip install requests python-dotenv

create .env:
GEMINI_API_KEY="your_key_here"

run:
python main.py

========================================

usage

just type whatever you want. literally anything. gefirsik will generate code and run it.

want to list files? say "list all files in downloads"
want to send a message? say "send hello to mom via sms"
want to automate something? describe it.

type logs to see what happened.
type exit or quit to get out.

========================================

the catch

you're running code written by an AI. on your phone. it might do exactly what you want. it might also do something unexpected.

so maybe don't ask it to delete system files or post your nudes to instagram.

check logs/gefirsik.log if something goes sideways.

========================================

why the name

gefirsik. sounds like a clumsy assistant who tries really hard. and that's exactly what this is.

========================================

that's it. go break things (responsibly).
