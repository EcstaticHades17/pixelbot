##This is how you should create your interface to whatever website/program you want to connect to

#connect():
this is for managing the connection, login and whatsoever

#getcountdown(): -> int
most projects like r/place have a time restriction.
should return a time in seconds
if there is no restriction, return 0

#send(x, y, r, g, b):
send the pixels (r, g, b) to the designated coordinates(x, y)
you may implement color flattening / color association

#check(x, y, r, g, b): -> bool
check if the current color of the designated pixel and the given color match
return True / False
