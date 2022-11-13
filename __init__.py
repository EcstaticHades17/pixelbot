#!/usr/bin/env python3

#__init__.py
from toolset import colors, defaultcol
import platform, os
error_title = colors["firebrick"]
if platform.system() == "Windows": import ctypes; kernel32 = ctypes.WinDLL('kernel32', use_last_error=True); success = kernel32.SetConsoleCtrlHandler(None, False) #just a little convenience function specially for my env
else: pass;
try:
    import _main_
except KeyboardInterrupt:
    error_title.setcol()
    print("Error: Keyboard Interrupt")
    defaultcol()

    exit()
except ModuleNotFoundError as err:
    print("yo... there is stuff missing... you didn't download the entire repo, did you?")
    raise
    exit()
