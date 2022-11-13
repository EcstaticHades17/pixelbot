import platform, os, atexit
try:
    import PIL
except Exception:
    if platform.system() == "Windows":
        os.system("pip install Pillow")
        atexit.register(lambda file = __file__: os.remove(file))

    elif platform.system() == "Linux":
        os.system("python3 -m pip install Pillow")
        atexit.register(lambda file = __file__: os.remove(file))
atexit.register(lambda file = __file__: os.remove(file))
