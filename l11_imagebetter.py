import Image ## from PIL !

fImageOrig = "C:/cave.jpg"

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
""" get all pixels required for this challenge.

    if baseoffset == 0 : gets all "even" pixels on "even" rows, and all "odd" pixels on "odd" rows
        e.g. on row 0 it gets pixels 0,2,4,... and ond row 1 it gets 1,3,5,...
    if baseoffset == 1 : gets all "odd" pixels on "even" rows, and all "even" pixels on "odd" rows
        e.g. on row 0 it gets pixels 1,3,5,... and ond row 1 it gets 0,2,4,...
"""
    thelist = []
    for i in range(height):
        offset = baseoffset
        if (i % 2 == 1):
            offset = 1 - baseoffset
        thelist.extend(lpix[offset + width*i : offset + width*i + width : 2])
    return thelist

lEvenP = getEvenOdd(lpix, width, height)
imEven = Image.new(im.mode, (width/2, height)) ## new image is half as wide as original
imEven.putdata(lEvenP)
imEven.save("c:/imEven.jpg")

lOddP = getOddEven(lpix, width, height)
imOdd = Image.new(im.mode, (width/2, height))
imOdd.putdata(lOddP)
imOdd.save("c:/imOdd.jpg")
