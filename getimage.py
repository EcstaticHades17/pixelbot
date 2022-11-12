#!/usr/bin/env python3
#getimage.py
from PIL import Image
import os
import random
import toolset

await_input = toolset.colors["darkorchid1"]
error_title = toolset.colors["firebrick"]
error_desc = toolset.colors["maroon"]
inputt = toolset.colors["mediumpurple"]
status = toolset.colors["gold3"]
random = toolset.colors["darkorange4"]
wtf = toolset.colors["teal"]
def imageprompt(UI, path=False):
    if UI == True:
        await_input.setcol()
        print("please provide the path to the image HERE:", end="   " )
        inputt.setcol()
        path = input()
        toolset.defaultcol()
    elif path == None and UI == False:
        error_title.setcol()
        print("     Error:")
        error_desc.setcol()
        print("Incomplete or missing Arguments: picture")
        toolset.defaultcol()
        exit(0)
    else:
        pass
    try:
        status.setcol()
        print("processing...")
        toolset.defaultcol()
        img = Image.open(path)
        size = img.size
        return img, size
    except Exception:
        error_title.setcol()
        print("There seems to be something wrong with the Image path.")
        error_title.setcol()
        print("     Error:")
        if not os.path.isfile(path):
            error_desc.setcol()
            print("     The file specified does not exist")
            print()
            responses = [
            "---How is this Program supposed to work this way?",
            "---You understood the purpose of this program, Right?",
            "---Nani?!?!?!",
            "---Help Me",
            "---...",
            "---How many times did you enter the wrong path to get this message?"]
            random.setcol()
            print(random.choice(responses))
            toolset.defaultcol()
            exit()
        else:
            wtf.setcol()
            print("How did you get here?")
            toolset.defaultcol()
