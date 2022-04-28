#getimage.py
from PIL import Image
import os
import random
def imageprompt(path=False):
    if path == False:
        print("\033[0;35;40m")
        path = input("please provide the path to the image here: ")
        print("\033[0;37;40m")
    else:
        pass
    try:
        img = Image.open(path)
        print("processing...")
        return img, img.size
    except Exception:
        print("\033[0;33;40m")
        print("There seems to be something wrong with the Image path.")
        print("\033[0;31;40m")
        print("     Error:")
        if not os.path.isfile(path):
            print("     The file specified does not exist")
            print("")
            responses = [
            "---How is this Program supposed to work this way?",
            "---You understood the purpose of this program, Right?",
            "---Nani?!?!?!",
            "---Help Me",
            "---...",
            "---How many times did you enter the wrong path to get this message?"]
            print("\033[0;32;40m")
            print(random.choice(responses))
            print("\033[0;37;40m")
            exit()
        else:
            print("\033[0;37;40m")
            print("How did you get here?")
