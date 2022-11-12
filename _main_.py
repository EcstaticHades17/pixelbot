#!/usr/bin/env python3
#_main_.py
import writer
import getimage
import argparse
import os
from time import sleep
import gimmedahandler


parser = argparse.ArgumentParser(
description= "A simple bot to place pixels from a picture to whatever you want \n Please note to write files with their according filetypes",
epilog= "Have fun with my Bot",
prefix_chars="-/",
add_help=False
)

parser.add_argument("-?", "--help", action="help", help="Show this help message")
parser.add_argument("--User_Interface", "-ui", action="store_true", dest="UI", help="Wether or not you will use the built-in User Interface. If given, will ignore all other parameters.")
parser.add_argument("-s", "--silence", "-s", action="store_true", dest="silence", help="If this parameter is given, the Program will not output anyting (exept fatal errors)")
parser.add_argument("-p", "--picture", type=str, dest="inpath", action="store", help="The path of the picture you want the Bot to draw.")
parser.add_argument("-h", "--handler", type=str, dest="handler", action="store", help="The file name of the handler that the Bot will use to draw your image.")
parser.add_argument("-sx", "--startx", type=int, dest="startx", action="store", help="The x coordinate of the top left corner of the canvas \n that the bot will draw your image into")
parser.add_argument("-sy", "--starty", type=int, dest="starty", action="store", help="The y coordinate of the top left corner of the canvas \n that the bot will draw your image into")
parser.add_argument("-ex", "--endx", type=int, dest="endx", action="store", help="The x coordinate of the bottom right corner of the canvas \n that the bot will draw your image into")
parser.add_argument("-ey", "--endy", type=int, dest="endy", action="store", help="The y coordinate of the bottom right corner of the canvas \n that the bot will draw your image into")
args = parser.parse_args()
#print("hehe", flush=True)
if args.UI and args.silence:
    while True:
        sleep(1)
        #how you gonna use a invisible UI???
if args.UI == False and args.inpath == None and args.handler == None and args.startx == None and args.starty == None:
    parser.parse_args(["-?"])
#print(args.handler)
if args.UI:
    image, size = getimage.imageprompt(args.UI)
    handler = gimmedahandler.gethandler(args.handler, args.UI)
    #print(handler)
    startx, starty, endx, endy = writer.getcanvas(args.UI, args.startx, args.starty, args.endx, args.endy)
    writer.write(image, handler, startx, starty, endx, endy, size, args.UI, args.silence)
else:
    handler = gimmedahandler.gethandler(args.handler, args.UI)
    image, size = getimage.imageprompt(args.UI, args.inpath)
    startx, starty, endx, endy = writer.getcanvas(args.UI, args.startx, args.starty, args.endx, args.endy)
    writer.write(image, handler, startx, starty, endx, endy ,size, args.UI, args.silence)
