#!/usr/bin/env python3
#_main_.py
import writer
import getimage
import argparse
import os
from time import sleep
import gimmedahandler   #import shit

##set up the parser
parser = argparse.ArgumentParser(
description= "A simple bot to place pixels from a picture to whatever you want \n Please note to write files with their according filetypes",
epilog= "Have fun with my Bot",
prefix_chars="-/",
add_help=False
)
# add arguments to the parser
parser.add_argument("-?", "--help", action="help", help="Show this help message")
parser.add_argument("--User_Interface", "-ui", action="store_true", dest="UI", help="Wether or not you will use the built-in User Interface. If given, will ignore all other parameters.")
parser.add_argument("-s", "--silence", "-s", action="store_true", dest="silence", help="If this parameter is given, the Program will not output anyting (exept fatal errors)")
parser.add_argument("-nc", "--no_colors", action="store_true", dest="nc", help="Wether to not use custom text coloring(e.g. if the output is saved to a file)")
parser.add_argument("-p", "--picture", type=str, dest="inpath", action="store", help="The path of the picture you want the Bot to draw.")
parser.add_argument("-h", "--handler", type=str, dest="handler", action="store", help="The file name of the handler that the Bot will use to draw your image.")
parser.add_argument("-sx", "--startx", type=int, dest="startx", action="store", help="The x coordinate of the top left corner of the canvas \n that the bot will draw your image into")
parser.add_argument("-sy", "--starty", type=int, dest="starty", action="store", help="The y coordinate of the top left corner of the canvas \n that the bot will draw your image into")
parser.add_argument("-ex", "--endx", type=int, dest="endx", action="store", help="The x coordinate of the bottom right corner of the canvas \n that the bot will draw your image into")
parser.add_argument("-ey", "--endy", type=int, dest="endy", action="store", help="The y coordinate of the bottom right corner of the canvas \n that the bot will draw your image into")
args = parser.parse_args() #parse the given arguments
#print("hehe", flush=True)
if args.UI and args.silence:
    while True:
        sleep(1)
        #how you gonna use a invisible UI???
if args.nc:     #creating a temporary file so that the toolset module knows wether or not to use custom colouring
    f = open("nc.temp", "x")
    f.close()
if args.UI == False and args.inpath == None and args.handler == None and args.startx == None and args.starty == None:
    parser.parse_args(["-?"]) #return the help page if no args are given
#print(args.handler)
if args.UI:
    image, size = getimage.imageprompt(args.UI) #getting the image stuff
    handler = gimmedahandler.gethandler(args.handler, args.UI) #retriveving the handler
    #print(handler)
    startx, starty, endx, endy = writer.getcanvas(args.UI, args.startx, args.starty, args.endx, args.endy) # retrieving the info about the canvas coordinates from the user
    writer.write(image, handler, startx, starty, endx, endy, size, args.UI, args.silence) #giving shit to the writing algorithms
    if args.nc:     #removing the temporary file
        os.remove("./nc.temp")
else:
    handler = gimmedahandler.gethandler(args.handler, args.UI) #prepping handler
    image, size = getimage.imageprompt(args.UI, args.inpath) #prepping the given img
    startx, starty, endx, endy = writer.getcanvas(args.UI, args.startx, args.starty, args.endx, args.endy) #checking the coords
    writer.write(image, handler, startx, starty, endx, endy ,size, args.UI, args.silence) #writing the image to the canvas
    if args.nc:      #removing the temporary file
        os.remove("./nc.temp")
