



def helpmsg(args=False):
    if args == False:
        pass
    else:
        if args[1] == "-h" or args[1] == "--help" or args[1] == "help" or args[1] == "h":
            msg = """message"""
            print(msg)
            exit()
        else:
            pass
