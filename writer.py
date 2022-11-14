#!/usr/bin/env python3

#writer.py
import random
import PIL
from time import sleep
import os
import gimmedahandler
import toolset
await_input = toolset.colors["darkorchid1"]
inputt = toolset.colors["mediumpurple"]
error_title = toolset.colors["firebrick"]
error_desc = toolset.colors["maroon"]
status = toolset.colors["gold3"]
random = toolset.colors["darkorange4"]
check = toolset.colors["limegreen"]
maintenancecol = toolset.colors["indianred"]
success = toolset.colors["olivedrab1"]
wtf = toolset.colors["teal"]

def write(img, handlerpath, sx, sy, ex, ey, size, UI, silence=False):
    try: #import the handler
        handlerfile = gimmedahandler.handler(handlerpath, UI)
        actor = __import__(handlerfile)
        status.setcol()
        print("Handler imported successfully")
    except ModuleNotFoundError: #the rare case that something went wrong
        wtf.setcolor()
        print("something is wrong with the given handler path but idk")
        toolset.defaultcol()

    finally:
        sizex, sizey = size
        if ex == None or ex == "" or ey == None or ey == "": #check wether or not the end of the canvas was given and generate them if needed
            if not silence:
                print("Generating bottom right corner of the canvas...")
            else:
                pass
            ex = sx + sizex
            ey = sy + sizey
            #print(sx)
            #print(sy)
            #print(ex)
            #print(ey)
            #print(sizex)
            #print(sizey)
        if (ex - sx) == sizex and (ey - sy) == sizey: #check if the size of the given canvas matches the size of the picture
            pass
        else:
            error_title.setcol()
            print("Error:")
            error_desc.setcol()
            print("It seems like the size of the image and the size of the provided area mismatch")
            toolset.defaultcol()
            exit()


        width, height = size
        pixel_values = img.getdata()
        if not silece:
            status.setcol()
            print("Initializing connection...")
        actor.connect()
        ##preparations
        tx = sx
        ty = sy
        rx = 0
        ry = 0
        #print(ey)
        num = 1
        maintenance = {}
        if silence: #write the picture in silent mode

            for y in range(sy, ey):
                for x in range(sx, ex):
                    sleep(actor.getcountdown())
                    r, g, b, opacity = img.getpixel((rx, ry))
                    if opacity > 50:
                        actor.send(tx, ty, r, g, b)
                        maintenance[num] = (tx, ty, r, g, b)
                        num += 1
                        for pixel in range(1, num):
                            x2, y2, r2, g2, b2 = maintenance[pixel]
                            if actor.check(x2, y2, r2, g2, b2):
                                pass
                            else:
                                sleep(actor.getcountdown())
                                maintenancecol.setcol()
                                actor.send(r2, g2, b2)
                    else:
                        pass
                    tx += 1
                    rx += 1
                ty -= 1
                ry += 1
                tx = sx
                rx = 0
            success.setcol()
            print("DONE")
            toolset.defaultcol()


        else: #write the picture in loud? mode

            print("printing...")
            for y in range(sy, ey):
                for x in range(sx, ex):
                    status.setcol()
                    print("Waiting for the wait to finish")
                    sleep(actor.getcountdown())
                    r, g, b, opacity = img.getpixel((rx, ry))
                    if opacity > 50:
                        #print(x)
                        #print(y)
                        #print(rx)
                        #print(ry)
                        #print(type(x))
                        #print(img.getpixel((rx, ry)))
                        check.setcol()
                        print("Sending pixel(" + str(tx) + "/" + str(ty) + ")")
                        actor.send(tx, ty, r, g, b)
                        maintenance[num] = (tx, ty, r, g, b)
                        #print(maintenance[num])
                        #print(num)
                        num += 1
                        for pixel in range(1, num):
                            x2, y2, r2, g2, b2 = maintenance[pixel]
                            status.setcol()
                            print(f"Checking pixel({str(x2)} / {str(y2)})")
                            if actor.check(x2, y2, r2, g2, b2):
                                pass
                            else:
                                status.setcol()
                                print("Waiting for the wait to finish")
                                sleep(actor.getcountdown())
                                maintenancecol.setcol()
                                print(f"Repairing pixel({str(x2)} / {str(y2)})")
                                actor.send(r2, g2, b2)
                    else:
                        print(f"skipping pixel {str(tx)} / {str(ty)} for lack of opacity")
                        pass
                    tx += 1
                    rx += 1
                ty -= 1
                ry += 1
                tx = sx
                rx = 0
            success.setcol()
            print("DONE")
            toolset.defaultcol()

def getcanvas(UI, sx, sy, ex, ey): #getting the canvas info
    if UI:
        await_input.setcol()
        print("Please enter the x-coordinate of the top left corner in the picture canvas:", end=" "); inputt.setcol() #user input
        sx = input()
        print()
        await_input.setcol()
        print("Please enter the y-coordinate of the top left corner in the picture canvas:", end=" "); inputt.setcol() #user input
        sy = input()
        print()
        await_input.setcol()
        print("Please enter the x-coordinate of the bottom right corner in the picture canvas:", end=" "); inputt.setcol() #user input
        ex = input()
        print()
        await_input.setcol()
        print("Please enter the y-coordinate of the bottom right corner in the picture canvas:", end=" "); inputt.setcol() #user input
        ey = input()
        toolset.defaultcol()
        pass
        try: #some checks
            sx = int(sx)
            sy = int(sy)
            if not ex == "" and not ey == "":
                ex = int(ex)
                ey = int(ey)
        except Exception:
            error_title.setcol()
            print("     Error:")
            error_desc.setcol()
            print("The given Values are or contain invalid Caracters")
            toolset.defaultcol()
            exit()
        if sx == "" or sy == "":
            error_title.setcol()
            print("Error:", end=" ")
            error_desc.setcol()
            print("Damn you so funny (Check your input dumbass)")
            toolset.defaultcol()
            exit()
        return sx, sy, ex, ey
    elif not sx == None and not sy == None:
        return sx, sy, ex, ey
    else: #raising an error
        error_title.setcol()
        print("     Error:")
        error_desc.setcol()
        print("Incomplete or missing Arguments: startx and/or starty")
        toolset.defaultcol()
        exit(0)
