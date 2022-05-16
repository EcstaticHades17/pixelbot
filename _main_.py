#__init__.py
import writer
import getimage
from helpmessagehandler import *
import sys
if len(sys.argv) == 3 or len(sys.argv) > 3:
    helpmsg(sys.argv)
else:
    pass


if len(sys.argv) == 3:
    inpath = sys.argv[1]
    handler = sys.argv[2]
    image, size = getimage.imageprompt(inpath)
    startx, starty, endx, endy = writer.getcanvas()
    writer.write(image, handler, startx, starty, endx, endy)
elif len(sys.argv) > 3:
    print("\033[0;33;40m")
    print("""   You provided too many arguments.
    The Program will try to use the first Argument as Path to the Image, and the second as the Path to a external Pixel-Art Handler.
    Read the interface.md for further instructions about how to create a Pixel-Art-Handler.
    Please Note that it is also possible to use this program interactively.""")
    print("\033[0;37;40m")
    inpath = sys.argv[1]
    image, size = getimage.imageprompt(inpath)
    handler = writer.gethandler(sys.argv)
    startx, starty, endx, endy = writer.getcanvas()
    writer.write(image, handler, startx, starty, endx, endy)
else:
    print("pront")
    image, size = getimage.imageprompt()
    handler = writer.gethandler()
    startx, starty, endx, endy = writer.getcanvas()
    writer.write(image, handler, startx, starty, endx, endy)
