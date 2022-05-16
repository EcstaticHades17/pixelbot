#gimmedahandler.py
import random
import os

def handler(handler):
    try:
        exec(handler.open().read())
    except Exception:
        if handler == "":
            print("\033[0;32;40m")
            responses = [
        "Error: No Communucation interface found",
        "Who ate my Communication Interface?",
        "https://www.google.com/search?q=Communication+Interface",
        "huh?"
            ]
            print(random.choice(responses))
            print("\033[0;37;40m")
            print("MT String (try to say it)")
        elif handler[0] == "/":
            handler = handler.replace("/", "", 1)
            exec(handler.open().read())
        elif os.path.isfile(handler):
            print("The file given is not a Pyhton Executable")
        elif os.path.isdir(handler):
            print("\033[0;32;40m")
            responses = [
        "Error: No Communucation interface found",
        "Who ate my Communication Interface?",
        "https://www.google.com/search?q=Communication+Interface",
        "huh?"
            ]
            print(random.choice(responses))
            print("\033[0;37;40m")
            print("Importing directories as handler is currently not supported")
