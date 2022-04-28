#__init__.py
import canvaswriter
import getimage
from helpmessagehandler import *
import sys

helpmsg(sys.argv)


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
else:
    image, size = getimage.imageprompt()
    print(size)
