try:
    exec(open("__main__.py").read())
except KeyboardInterrupt:
    print("\033[0;31;40m Error: Keyboard Interrupt \033[0;37;40m")
    exit()
