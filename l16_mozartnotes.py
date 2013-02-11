import PIL
from PIL import Image

im = Image.open("l16/mozart.gif")
print im.size, im.mode

g = im.convert("RGB")
l = list(g.getdata())

## almost-whites
poss = [(x,x,x) for x in range(240, 255)] ## don't include 255 !!

things = []

globidx = 0

while globidx < len(l):
    foundstuff = []
    for item in poss:
        try:
            ## try to find a "white"
            idx = l.index(item, globidx)
            ## found one
            foundstuff.append(idx) ## remember we found THIS one
        except ValueError:
            pass
    if foundstuff == []:
        break ## none of the poss found, so we're done
    ## we're only interested in the minimum index ("first" one found)
    it = min(foundstuff)

    print "found : at pos", it, ":", l[it:it+7]
    ## append this thingie, including position
    things.append((l[it:it+7], it))
    globidx = it + 7
    
print "*** total found :", len(things)

f = open("l16/blocks.txt", "w")
f.writelines("\n".join(map(str, things)))
f.close()
