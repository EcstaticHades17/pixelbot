This is how you should create your interface to whatever website/program you want to connect to

connect():
this is for managing the connection, login and whatsoever

getcountdown():
most projects like r/place have a time restriction.
should put out a time in seconds
if there is no restriction, put out 0

send(x, y, r, g, b):
send the pixels (r, g, b) to the designated coordinates(x, y)
you may implement color flattening / color association

get(x, y):
get the color of a pixel based on the coordinates given
should return an rgb value
