import PIL
from PIL import Image

def resizeImage(fni, fno, size):
    im = Image.open(fni)
    im = im.resize(size)
    im.save(fno)

def makeSpiral(pixdata, width, height):
    top = 0
    right = width-1
    bottom = width*height-1
    left = bottom-width+1 

    print "width, height :", width, height
    print "top", top, "| right", right, "| bottom", bottom, "| left", left

    l = pixdata
    lnew = []

    while (top <= right):
        ## go left-right. use top to indicate start!!
        lnew.extend(l[top : right+1 : 1]) ## make sure to INCLUDE right
        ## next "top" will be one line down, one pixel right
        top += width
        top += 1
        if (right >= bottom):
            break
        ## go top-bottom. use right+width to indicate start!!
        lnew.extend(l[right+width : bottom+1 : width]) ## make sure to INCLUDE bottom
        ## next "right" will be one line down, one pixel left
        right += width
        right -= 1
        if (left >= bottom):
            break
        ## go right-left. use bottom-1 to indicate start !!
        lnew.extend(l[bottom-1 : left-1 : -1]) ## make sure to INCLUDE left
        ## next "bottom" will be one line up, one pixel left
        bottom -= width
        bottom -= 1
        if (top >= left):
            break
        ## go bottom-top. use left-width to indicate start!!
        lnew.extend(l[left-width : top-width  : -width]) ## make sure to INCLUDE top
        ## next "left" will be one line up, one pixel right
        left -= width
        left += 1

    return lnew


def makeUnSpiral(pixdata, width, height):
    top = 0
    right = width-1
    bottom = width*height-1
    left = bottom-width+1 

    print "width, height :", width, height
    print "top", top, "| right", right, "| bottom", bottom, "| left", left

    l = pixdata
    lnew = [0] * len(pixdata) ## new pic should have same length

    cnt = 0

    while (top <= right):
        ## go left-right. use top to indicate start!!
        ## make sure to INCLUDE right
        for i in range(top, right+1, 1):
            lnew[i] = l[cnt]
            cnt += 1
        ## next "top" will be one line down, one pixel right
        top += width
        top += 1
        if (right >= bottom):
            break
        ## go top-bottom. use right+width to indicate start!!
        ## make sure to INCLUDE bottom
        for i in range(right+width, bottom+1, width):
            lnew[i] = l[cnt]
            cnt += 1
        ## next "right" will be one line down, one pixel left
        right += width
        right -= 1
        if (left >= bottom):
            break
        ## go right-left. use bottom-1 to indicate start !!
        ## make sure to INCLUDE left
        for i in range(bottom-1, left-1, -1):
            lnew[i] = l[cnt]
            cnt += 1
        ## next "bottom" will be one line up, one pixel left
        bottom -= width
        bottom -= 1
        if (top >= left):
            break
        ## go bottom-top. use left-width to indicate start!!
        ## make sure to INCLUDE top
        for i in range(left-width, top-width, -width):
            lnew[i] = l[cnt]
            cnt += 1
        ## next "left" will be one line up, one pixel right
        left -= width
        left += 1

    print "final cnt is at", cnt

    return lnew


def runTests():

    for i in range(1,6):
        for j in range(1,6):

            width, height = i, j

            print "*" * 40
            print "*** Doing width, height", width, ",", height, " ***"
            print "*" * 40
            
            l = range(width*height)

            print "*** spiralling ..."
            lnew = makeSpiral(l, width, height)
            print "length of spiraled pic =", len(lnew)
            print lnew

            print

            print "*** un-spiralling ..."
            lo = makeUnSpiral(lnew, width, height)
            print "length of unspiraled pic =", len(lo)
            print lo

            assert l == lo

##runTests()

f = Image.open("C:\\wire.png")
l = list(f.getdata())

width, height = 100, 100

lnew = makeUnSpiral(l, width, height)

g = Image.new("RGB", (width, height))
g.putdata(lnew)
g.save("C:\\aha_un_spiral" + str(height) + ".png")
