from PIL import Image
import bz2

im = Image.open("C:/zigzag.gif")
l = list(im.getdata())
    ## l now contains a list of pixels,
    ## which are indexes to the color table since this is a paletted image
pal = im.palette
colors = map(ord, pal.tostring()[::3])
    ## since the colors in this image are all greys (R=G=B), we only
    ## need one component (e.g. R)

def walkIt(table1=l, table2=colors):
    pos = 0
    found = []
    right = []
    cnt = 0
    while pos < len(table1)-1:
        pixel = table1[pos]
        color = table2[pixel]
        pos += 1
        ## check if the next pixel's color index =
        ## the "real" color of the previous one
        if table1[pos] == color:
            continue
        else:
            ## anomaly found -> data!
            pixel = table1[pos]
            found.append(pixel)
            ## also keep the "right" colors!!
            right.append(abs(pixel - color))
    ##        print "found at pos %i : '%s' (%d)" % (pos, chr(pixel), pixel)
    print "len of found = %d" % len(found)
    print "len of right = %d" % len(right)
    return (found, right)

def walkItFindNormal(table1=l, table2=colors):
    pos = 0
    normal = []
    cnt = 0
    while pos < len(table1)-1:
        pixel = table1[pos]
        normal.append(pixel)
        color = table2[pixel]
        pos += 1
        ## move forward until we found a "normal" pixel
        while table1[pos] != color:
            pos += 1
            if pos >= len(l):
                break
    print "len of normal = %d" % len(normal)
    return normal

def writeFiles(found):
    data = "".join(map(chr, found))
    ## just show a little bit of data
    print data[:10]

    fo = open("C:/data.bz2", "wb")
    fo.write(data)
    fo.close()

    uncomp = bz2.decompress(data)
    fo = open("C:/words.txt", "w")
    fo.write(uncomp)
    fo.close()

