#writer.py
import random
import PIL
from time import sleep
import os
import gimmedahandler
def write(img, handler, sx, sy, ex, ey):
    try:
        gimmedahandler.handler(handler)
        
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
        maintenance = {}
        for y in range(sy, ey):
            for x in range(sx, ex):
                sleep(handler.getcountdown())
                r, g, b, = pixel_values[width*y+x]
                handler.send(tx, ty, r, g, b)
                num = x*y
                maintenance[num] = (tx, ty, r, g, b)
                for pixel in range(num):
                    x2, y2, r2, g2, b2 = maintenance[pixel]
                    if r2 == handler.get(x2, y2)[0] and g2 == handler.get(x2, y2)[1] and b2 == handler.get(x2, y2)[2]:
                        pass
                    else:
                        sleep(handler.getcountdown())
                        handler.send(r2, g2, b2)
                tx += 1
            ty += 1


def gethandler(args=False):
    if args == False:
        print("\033[0;32;40m")
        print("The Program has currently no built-in Interface to communicate with a Pixel-Art Service.")
        handler = input("\033[0;35;40m Please provide the path to a exernal Communication Interface HERE: \033[0;37;40m")
    else:
        handler = args
        return handler
def getcanvas():
    sx = input("\033[0;35;40m Please enter the x-coordinate of the top left corner in the picture canvas: \033[0;37;40m")
    sy = input("\033[0;35;40m Please enter the y-coordinate of the top left corner in the picture canvas: \033[0;37;40m")
    ex = input("\033[0;35;40m Please enter the x-coordinate of the bottom right corner in the picture canvas: \033[0;37;40m")
    ey = input("\033[0;35;40m Please enter the y-coordinate of the bottom right corner in the picture canvas: \033[0;37;40m")
    try:
        sx = int(sx)
        sy = int(sy)
        ex = int(ex)
        ey = int(ey)
    except Exception:
        print("\033[0;31;40m")
        print("     Error:")
        print("The given Values are or contain invalid Caracters")
        print("\033[0;37;40m")
        exit()
    if sx == "" or sy == "" or ex == "" or ey == "":
        print("Error: Yo")
        exit()
    return sx, sy, ex, ey
