## image quickie!
## install PIL (Python Imaging Library) first. Supercool lib

import Image ## from Pil !

fImageOrig = "C:\\evil1.jpg"

im = Image.open(fImageOrig)
print im.size, im.mode

width, height = im.size

## get pixel list
lpix = list(im.getdata())

def getEvenOdd(lpix, width, height):
    return getPixels(lpix, width, height, 0)

def getOddEven(lpix, width, height):
    return getPixels(lpix, width, height, 1)

def getPixels(lpix, width, height, baseoffset):
    thelist = []
    for i in range(height):
        offset = baseoffset
        if (i % 6 in [3,4,5]):
            offset = 1 - baseoffset
        ## get all "even" pixels on rows like 0,1,2, and all
        ## "odd" pixels on rows like 3,4,5
        thelist.extend(lpix[offset + width*i : offset + width*i + width : 2])
    return thelist
        
##l0 = getEvenOdd(lpix, width, height)
##l1 = getOddEven(lpix, width, height)
l0 = lpix[::2]
l1 = lpix[1::2]

im0 = Image.new(im.mode, (width/2, height))
im0.putdata(l0)
im0.save("c:\\ev0.jpg")

im1 = Image.new(im.mode, (width/2, height))
im1.putdata(l1)
im1.save("c:\\ev1.jpg")

def getAnXthPartHeight(lpix, width, height, startline, x=6):
    l = []
    print width, height, startline
    for i in range(startline, height, x):
        l.extend(lpix[i*width : (i+1)*width])
    return l

def getAnXthPartWidth(lpix, width, height, startcol, x=8):
    print width, height, startcol
    return lpix[startcol::x]

magicheight = 5

listsEven = range(magicheight)
imagesEven = range(magicheight)
for i in range(magicheight):
    listsEven[i] = getAnXthPartHeight(l0, width/2, height, i, magicheight)
    imagesEven[i] = Image.new(im.mode, (width/2, height/magicheight))
    imagesEven[i].putdata(listsEven[i])
    imagesEven[i].save("c:\\evil_even_" + str(magicheight) + "_" + str(i) + ".jpg")
        
listsOdd = range(magicheight)
imagesOdd = range(magicheight)
for i in range(magicheight):
    listsOdd[i] = getAnXthPartHeight(l1, width/2, height, i, magicheight)
    imagesOdd[i] = Image.new(im.mode, (width/2, height/magicheight))
    imagesOdd[i].putdata(listsOdd[i])
    imagesOdd[i].save("c:\\evil_odd_" + str(magicheight) + "_" + str(i) + ".jpg")


magicwidth = 4

for j in range(magicheight):
    listsEvenJ = range(magicwidth)
    imagesEvenJ = range(magicwidth)
    for i in range(magicwidth):
        listsEvenJ[i] = getAnXthPartWidth(listsEven[j], width/2, height, i, magicwidth)
        imagesEvenJ[i] = Image.new(im.mode, ((width/2)/magicwidth, height/magicheight))
        imagesEvenJ[i].putdata(listsEvenJ[i])
        imagesEvenJ[i].save("c:\\evil_even_" + str(magicheight) + "_" + \
                        str(magicwidth) + "_" + str(i) + "_" + str(j) + ".jpg")

for j in range(magicheight):
    listsOddJ = range(magicwidth)
    imagesOddJ = range(magicwidth)
    for i in range(magicwidth):
        listsOddJ[i] = getAnXthPartWidth(listsOdd[j], width/2, height, i, magicwidth)
        imagesOddJ[i] = Image.new(im.mode, ((width/2)/magicwidth, height/magicheight))
        imagesOddJ[i].putdata(listsOddJ[i])
        imagesOddJ[i].save("c:\\evil_odd_" + str(magicheight) + "_" + \
                        str(magicwidth) + "_" + str(i) + "_" + str(j) + ".jpg")
