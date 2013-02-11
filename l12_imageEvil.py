## image quickie!
## install PIL (Python Imaging Library) first. Supercool lib

import Image ## from Pil !

fImageOrig = "C:\\evil.jpg"

im = Image.open(fImageOrig)
print im.size, im.mode

width, height = im.size

## get pixel list
lpix = list(im.getdata())

## get 0-lines
l0 = []
for i in range(0,height,3):
    ## get all "even" pixels on "even" rows, and all "odd" pixels on "odd" rows
    l0.extend(lpix[width*i : width*i + width])
        
## get 1-lines
l1 = []
for i in range(1,height,3):
    ## get all "even" pixels on "even" rows, and all "odd" pixels on "odd" rows
    l1.extend(lpix[width*i : width*i + width])

## get 2-lines
l2 = []
for i in range(2,height,3):
    ## get all "even" pixels on "even" rows, and all "odd" pixels on "odd" rows
    l2.extend(lpix[width*i : width*i + width])

im0 = Image.new(im.mode, (width, height/3))
im0.putdata(l0)
im0.save("c:\\evil_0.jpg")

im1 = Image.new(im.mode, (width, height/3))
im1.putdata(l1)
im1.save("c:\\evil_1.jpg")

im2 = Image.new(im.mode, (width, height/3))
im2.putdata(l2)
im2.save("c:\\evil_2.jpg")

def getEvenOdd(lpix, width, height):
    return getPixels(lpix, width, height, 0)

def getOddEven(lpix, width, height):
    return getPixels(lpix, width, height, 1)

def getPixels(lpix, width, height, baseoffset):
    thelist = []
    for i in range(height):
        offset = baseoffset
        if (i % 2 == 1):
            offset = 1 - baseoffset
        ## get all "even" pixels on "even" rows, and all "odd" pixels on "odd" rows
        thelist.extend(lpix[offset + width*i : offset + width*i + width : 2])
    return thelist
        
l0_even = getEvenOdd(l0, width, height/3)
l0_odd = getOddEven(l0, width, height/3)

im0_even = Image.new(im.mode, (width/2, height/3))
im0_even.putdata(l0_even)
im0_even.save("c:\\evil_0_even.jpg")

im0_odd = Image.new(im.mode, (width/2, height/3))
im0_odd.putdata(l0_odd)
im0_odd.save("c:\\evil_0_odd.jpg")


l1_even = getEvenOdd(l1, width, height/3)
l1_odd = getOddEven(l1, width, height/3)

im1_even = Image.new(im.mode, (width/2, height/3))
im1_even.putdata(l1_even)
im1_even.save("c:\\evil_1_even.jpg")

im1_odd = Image.new(im.mode, (width/2, height/3))
im1_odd.putdata(l1_odd)
im1_odd.save("c:\\evil_1_odd.jpg")


l2_even = getEvenOdd(l2, width, height/3)
l2_odd = getOddEven(l2, width, height/3)

im2_even = Image.new(im.mode, (width/2, height/3))
im2_even.putdata(l2_even)
im2_even.save("c:\\evil_2_even.jpg")

im2_odd = Image.new(im.mode, (width/2, height/3))
im2_odd.putdata(l2_odd)
im2_odd.save("c:\\evil_2_odd.jpg")



