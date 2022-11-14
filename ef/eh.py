#!/usr/bin/env python3

#eh.py
# a example for a handler. Useless and only for testing
def connect():
    print("")

def getcountdown():
    #return int(input("countdown in seconds?"))
    return 0.125

def send(x, y, r, g, b):
    print((x, y))
    print(f"RGB({r}, {g}, {b})")

def check(x, y, r, g, b):
    return True
