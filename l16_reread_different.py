from PIL import Image

f = open("C:/blocks.txt")

things = [eval(t) for t in f.readlines()]

f.close()

## make dict with x-pos for every y-pos (we get tuples of (y,x))
## note : we have to go to (y,x), because we only know all the y's are
## unique, NOT all the x's !!
things = [(t[1]/640, t[1]%640) for t in things]
d = dict(things)

def writeDict(name, d):
    dtxt = open(name, "w")
    k = d.keys()
    k.sort()
    for item in k:
        dtxt.write("%d -> %s\n" % (item, d[item]))
    dtxt.close()

writeDict("C:/d.txt", d)

im = Image.open("C:/mozart.gif")
print im.size, im.mode
width, height = im.size

g = im.convert("RGB")
l = list(g.getdata())
lnew = []

#* rotate the lines according to the x positions !! *#

## sort the y values
ys = d.keys()
print len(ys)
ys.sort()
print len(ys)

## build a list of the rotated lines
for y in ys:
    start = d[y]
    ## "rotate" the line to the left
    lnew.extend(l[y*width + start : y*width + width])
    lnew.extend(l[y*width : y*width + start])

## write out the shuffled image
immod = Image.new("RGB", (width, height))
immod.putdata(lnew)
immod.save("C:/mozart_rotated.gif")

## done!
