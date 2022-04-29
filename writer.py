#writer.py
import random
import PIL
from time import sleep
def write(img, handler, sx, sy, ex, ey):
    try:
        module = "import "+handler+" as handler"
        exec(module)
    except Exception:
        print("\033[0;32;40m")
        responses = [
        "Error: No Communucation interface found",
        "Who ate my Communication Interface?"
        "https://www.google.com/search?q=Communication+Interface",
        "huh?"
        ]
        print(random.choice(responses))
        print("\033[0;37;40m")
        raise Exception("The program was not given a interface")
    else:
        sizex, sizey = img.size
        if (sx - ex) == sizex and (sy - ey) == sizey:
            pass
        else:
            print("\033[0;33;40m")
            print("It seems like the size of the image and the size of the provided area mismatch")
            exit()
        width, height = img.size
        pixel_values = list(img.getdata())
        handler.connect()
        tx = sx
        ty = sy

        for y in range(sy, ey):
            for x in range(sx, ex):
                sleep(handler.getcountdown())
                handler.send(tx, ty, pixel_values[width*y+x])
                tx += 1
            ty += 1
def gethandler():
    print("\033[0;32;40m")
    print("The Program has currently no built-in Interface to communicate with a Pixel-Art Service.")
    handler = input("\033[0;35;40m Please provide the path to a exernal Communication Interface HERE: \036[0;32;40m")
    return handler
def getcanvas():
    sx = input("\033[0;35;40m Please enter the x-coordinate of the top left corner in the picture canvas: \036[0;32;40m")
    sy = input("\033[0;35;40m Please enter the y-coordinate of the top left corner in the picture canvas: \036[0;32;40m")
    ex = input("\033[0;35;40m Please enter the x-coordinate of the bottom right corner in the picture canvas: \036[0;32;40m")
    ey = input("\033[0;35;40m Please enter the y-coordinate of the bottom right corner in the picture canvas: \036[0;32;40m")
    return sx, sy, ex, ey
