# -*- coding: cp1252 -*-
from PIL import Image
import string
from string import ascii_letters
from string import ascii_uppercase
from string import ascii_lowercase
from string import printable

im = Image.open("C:/zigzag.gif")
l = list(im.getdata())
pal = im.palette
palS = pal.tostring()

## get all colors
colors = [(ord(palS[i]), ord(palS[i+1]), ord(palS[i+2])) for i in xrange(0, len(palS), 3)]
print colors          

## check that colors are only greys, in that case we don't need RGB
## but we can do with only R for instance
for col in colors:
    assert col[0] == col[1] == col[2], "oops, a not-grey found!!"

## only keep the red component
colors = [col[0] for col in colors]
print colors

## now try all possible strategies we can think of for "walking" the image
# 1) walk left-right
# 2) walk right-left
# 3) walk columns, top-down
# 4) walk columns, bottom-up
# 5) walk NE (wrapping around), until we arrive back at start
# 6) walk SE (wrapping around), until we arrive back at start
# 7) walk SW (wrapping around), until we arrive back at start
# 8) walk NW (wrapping around), until we arrive back at start
## for all cases : write out string to a file

fo = open("C:/walk_1_s.txt", "w")
s = "".join(map(chr, l))
fo.writelines(s)
fo.close()

def formatList(li):
    return "".join(["%4s" % str(i) for i in li])

fo = open("C:/walk_1_list.txt", "w")
sl = "\n".join([formatList(l[i:i+320]) for i in xrange(0, len(l), 320)])
fo.writelines(sl)
fo.close()               

#### find the blocks of 40 bytes that keep repeating !
##i = 1740
##while i < len(l):
##    if l[i] == 79 and l[i+1] == 48 and l[i+2] == 161:
##        print "found at %d = (%d, %d)" % (i, i%320, i/320)
##        ## check if this 40-byte block is repeated 6 times
##        for j in range(6):
##            assert(l[i + 40*j : i + 40*(j+1)] == l[i:i+40])
##        i += 240
##    i += 1    
            
## find our blocks of length 148 that keep repeating
## we need the indexes of these.
indexes_149 = []
fo = open("C:/walk_149bytes_blocks.txt", "w")
i=0
while i < len(l) and i+148 < len(l):
    if l[i] == 91 \
       and l[i+14:i+17] == [78, 250, 100] \
       and l[i+148] == 13 \
       and l[i+126] == 49:
        print i
        indexes_149.append(i)
        text = "%5d :" % i
        sl = text + formatList(l[i:i+149]) + "\n"
        fo.writelines(sl)
        i += 149
        continue
    i += 1    
fo.close()               

## now find suspicious blocks of length x that also keep repeating,
## in the REST of the "image"
indexes_57 = []
fo = open("C:/walk_57bytes_blocks.txt", "w")
i=0
while i < len(l) and i+56 < len(l):
    if i in indexes_149:
        print i, "is already in indexes_149!!",
        i += 149 ## skip search within this !
        print "new i :", i
        continue
    if l[i:i+3] == [215, 208, 203] \
       and l[i+56] == 13 \
       and l[i+13] == 70:
        ## only append if this is NOT a subpart of a 148-sequence
        for idx in indexes_149:
            if idx <= i < (idx + 149):
                break
        else:
            indexes_57.append(i)
            print i
            text = "%5d :" % i
            sl = text + formatList(l[i:i+57]) + "\n"
            fo.writelines(sl)
            i += 57
            continue
    i += 1    
fo.close()               


## now find suspicious blocks of length x that also keep repeating,
## in the REST of the "image"
indexes_9 = []
fo = open("C:/walk_9bytes_blocks.txt", "w")
i=0
while i < len(l) and i+9 < len(l):
    if i in indexes_149:
        print i, "is already in indexes_149!!",
        i += 149 ## skip search within this !
        print "new i :", i
        continue
    if i in indexes_57:
        print i, "is already in indexes_57!!",
        i += 57 ## skip search within this !
        print "new i :", i
        continue
    if l[i:i+9] == [148, 107, 188, 7, 41, 223, 117, 80, 10]:
        for idx in indexes_149:
            if idx <= i < (idx + 149):
                break
        else:
            for idx in indexes_57:
                if idx <= i < (idx + 57):
                    break
            else:
                indexes_9.append(i)
                print i
                text = "%5d :" % i
                sl = text + formatList(l[i:i+9]) + "\n"
                fo.writelines(sl)
                i += 9
                continue
    i += 1    
fo.close()
