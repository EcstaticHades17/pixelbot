#__init__.py
import writer
import getimage
from helpmessagehandler import *
import sys

if len(sys.argv) == 2 or len(sys.argv) > 2:
    helpmsg(sys.argv)
else:
    pass


if len(sys.argv) == 2:
    inpath = sys.argv[1]
    getimage.imageprompt(inpath)
elif len(sys.argv) > 2:
    print("\033[0;33;40m")
    print("""   You provided too many arguments.
    The Program will try to use the first Argument as Path to the Image.
    Please Note that it is also possible to use this program interactively.""")
    print("\033[0;37;40m")
    inpath = sys.argv[1]
    image, size = getimage.imageprompt(inpath)
    writer.write(image)
else:
    image, size = getimage.imageprompt()
    startx, starty, endx, endy = writer.getcanvas()
    writer.write(image, writer.gethandler(), startx, starty, endx, endy)
