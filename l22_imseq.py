from PIL import Image, ImageSequence
import turtle

stands = {
    (100, 100): 'N',
    (98, 100) : 'L',
    (102,100) : 'R',
    (100, 98) : 'U',
    (100, 102): 'D',
    (98, 98)  : 'LU',
    (102, 98) : 'RU',
    (98, 102) : 'LD',
    (102, 102): 'RD'
}

dist = 3

moves = {
    (100, 100): lambda (x,y) : (x,y),
    (98, 100) : lambda (x,y) : (x-dist, y),
    (102,100) : lambda (x,y) : (x+dist, y),
    (100, 98) : lambda (x,y) : (x, y-dist),
    (100, 102): lambda (x,y) : (x, y+dist),
    (98, 98)  : lambda (x,y) : (x-dist, y-dist),
    (102, 98) : lambda (x,y) : (x+dist, y-dist),
    (98, 102) : lambda (x,y) : (x-dist, y+dist),
    (102, 102): lambda (x,y) : (x+dist, y+dist)
}

imseq = ImageSequence.Iterator(Image.open("l22/white.gif"))
poss = []
coords = []
for im in imseq:
    l = list(im.getdata())
    ## there is exactly one pixel different from background color in
    ## each picture
    p = l.index(8)
    poss.append(p)
    coords.append((p%200, p/200))
    
print coords

## show "joystick movements"
seq = [stands[i] for i in coords]
s = "_".join(seq)
print s

## show "separate" movements (split by neutral position)
print "\n".join(s.split("N"))

basex=-150
basey=0

## now draw out the movements!
for p in coords:
    ## when we encounter a "neutral" position :
    ## move "one character" right
    if stands[p] == "N":
        turtle.up()
        basex, basey = basex + 60, basey
        x, y = basex, basey
        ## note : always use -y as y-coord, since the turtle module
        ## reverses the y-axis. Otherwise the picture is upside down
        turtle.goto((x,-y))
        turtle.down()
    else :
        x, y = moves[p]((x,y))
        turtle.goto((x,-y))
