import platform, os, atexit
try:
    import PIL
except Exception:
    if platform.system() == "Windows":
        os.system("pip install Pillow")  # install the Pillow imagin module in win format
        atexit.register(lambda file = __file__: os.remove(file)) #deletus

    elif platform.system() == "Linux":
        os.system("python3 -m pip install Pillow") # install the Pillow imagin module in win format
        atexit.register(lambda file = __file__: os.remove(file)) #deletus
atexit.register(lambda file = __file__: os.remove(file)) #deletus
