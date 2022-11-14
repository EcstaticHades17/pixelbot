#!/usr/bin/env python3

#gimmedahandler.py
import random
import sys
import toolset
import platform
import os
import toolset

await_input = toolset.colors["darkorchid1"]
error_title = toolset.colors["firebrick"]
error_desc = toolset.colors["maroon"]
inputt = toolset.colors["mediumpurple"]
status = toolset.colors["gold3"]
random = toolset.colors["darkorange4"]
wtf = toolset.colors["teal"]

def gethandler(handler, UI=False):
    if UI == True:
        status.setcol()
        print("The Program has currently no built-in Interface to communicate with a Pixel-Art Service.")
        await_input.setcol()
        print("Please provide the path to a exernal Communication Interface HERE:", end="   ") #geting user input
        inputt.setcol()
        handler = input()
        #print(handler)
        toolset.defaultcol()
        return handler
    else:
        return handler

def handler(handler, silence=False):
    #print(handler)
    check = handler[::-1]
    if handler == "": #invalid input
        responses = [   #random message
    "Error: No Communication interface found",
    "Who ate my Communication Interface?",
    "https://www.google.com/search?q=Communication+Interface",
    "huh?",
    "..."
        ]
        if not silence:  #checking if in silent mode
            random.setcol()
            print(random.choice(responses))
        error_title.setcol()
        print("Error:")
        error_desc.setcol()
        print("MT String (try to say it)") #returning the error
        toolset.defaultcol()
    elif handler[0] == "/" and not (platform.system() == "Linux"):  #making shure the path is not misspelled or smth
        handler = "." + handler
        handler = handler.split("/")
        handler.reverse()
        path = handler
        path.remove(handler[0])
        path.reverse()
        sys.path.insert(1, toolset.combine(path, "/"))
        file = handler
        file = file[0].strip()
        file = handler.split(".")
        file.reverse()
        file.remove(handler[0])
        file.reverse()
        file = toolset.combine(handler, ".")
        print(file, flush=True)
        return file
        pass
    elif handler[1] == ":" and platform.system() == "Windows":   #checking if the handler is on a different filesystem under windowss
        handler = handler.split("/")
        handler.reverse()
        path = handler
        path.remove(handler[0])
        path.reverse()
        sys.path.insert(1, toolset.combine(path, "/"))
        file = handler
        file = file[0].strip()
        file = handler.split(".")
        file.reverse()
        file.remove(handler[0])
        file.reverse()
        file = toolset.combine(handler, ".")
        print(file, flush=True)
        return file
        pass
    elif os.path.isfile(handler) and not check[:3] == "yp.":  #checks if the object is a file and if it ends with .py (yp. in reverse)
        error_title.setcol()
        print("Error:")
        error_desc.setcol()
        print("The file given is not a Python Executable")
        toolset.defaultcol()
    elif os.path.isdir(handler):
        sys.path.insert(1, handler)
        handler = handler.split("/")
        handler.reverse()
        handler = handler[0].strip()
        return handler
    elif "/" in handler:
        #print(handler)
        handler = handler.split("/")
        handler.reverse()
        #print(handler)
        path = handler[0:]
        #print(path)
        path.remove(path[0])
        #print(path)
        path.reverse()
        #print(path)
        sys.path.insert(1, toolset.combine(path, "/"))
        file = handler
        #print(file)
        file = file[0]
        #print(file)
        file = file.split(".")
        file.reverse()
        file.remove(file[0])
        file.reverse()
        #print(file)
        file = toolset.combine(file, ".")
        #print(file, flush=True)
        return file
    else: #the handler is most likely in the own folder
        sys.path.insert(1, "./")
        handler = handler.split(".")
        handler.reverse()
        handler.remove(handler[0])
        handler.reverse()
        handler = toolset.combine(handler, ".")
        #print(handler)
        return handler
