from PIL import Image

f = open("C:\\sounds.txt")

things = [eval(t) for t in f.readlines()]

f.close()

##things = [(t[0][0], t[0][6], t[1]) for t in things]

##ou = open("c:/details.txt", "w")
##for ti in things:
##    start, end, pos = ti
##    ou.write("pos %7d (x %3d, y %3d) : start = %15s, end = %15s\n" \
##          % (pos, pos%640, pos/640, start, end))
##ou.close()

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

## invert this dict to get x to y mappings
inv_d = {}
for k, v in d.items():
    inv_d.setdefault(v, []).append(k)

writeDict("C:/d_inv.txt", inv_d)

##inv_inv_d = {}
##for k in inv_d.keys():
##    for x in inv_d[k]:
##        inv_inv_d[x] = k
##
##assert d == inv_inv_d        


im = Image.open("C:/mozart.gif")
print im.size, im.mode
width, height = im.size

g = im.convert("RGB")
l = list(g.getdata())
lnew = []

#* swap lines according to the dict !! *#

## sort the x values
xs = inv_d.keys()
print len(xs)
xs.sort()
print len(xs)
## add lines to our list, according to the corresponding y-values
cnt=0
for x in xs:
    for y in inv_d[x]:
        lnew.extend(l[y*width : y*width + width])
        cnt += 1
print "cnt = %d" % cnt        

## write out the shuffled image
immod = Image.new("RGB", (width, height))
immod.putdata(lnew)
immod.save("C:/mozartmod.gif")

## done!
