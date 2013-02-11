import PIL
from PIL import Image
import operator

im = Image.open("C:/balloons.jpg")
width, height = im.size

l = list(im.getdata())

lleft  = []
lright = []

for y in range(height):
    lleft.extend(l[y*width : y*width + width/2])
    lright.extend(l[y*width + width/2 : y*width + width])

imL = Image.new("RGB", (width/2, height))
imR = Image.new("RGB", (width/2, height))

imL.putdata(lleft)
imR.putdata(lright)

imL.save("C:/left.jpg")
imR.save("C:/right.jpg")

imLDiff = Image.new("RGB", (width/2, height))
imRDiff = Image.new("RGB", (width/2, height))
imAbsDiff = Image.new("RGB", (width/2, height))
imXor   = Image.new("RGB", (width/2, height))
imRedDiff   = Image.new("RGB", (width/2, height))
imGreenDiff = Image.new("RGB", (width/2, height))
imBlueDiff  = Image.new("RGB", (width/2, height))
imTest  = Image.new("RGB", (width/2, height))

lLDiff = [(r1-r2, g1-g2, b1-b2) for (r1,g1,b1), (r2,g2,b2) in zip(lleft, lright)]
lRDiff = [(r2-r1, g2-g1, b2-b1) for (r1,g1,b1), (r2,g2,b2) in zip(lleft, lright)]
lAbsDiff = [(abs(r1-r2), abs(g1-g2), abs(b1-b2)) for (r1,g1,b1), (r2,g2,b2) in zip(lleft, lright)]
lXor   = [(r2^r1, g2^g1, b2^b1) for (r1,g1,b1), (r2,g2,b2) in zip(lleft, lright)]
lRedDiff   = [(r1-r2, 0, 0) for (r1,g1,b1), (r2,g2,b2) in zip(lleft, lright)]
lGreenDiff = [(0, g1-g2, 0) for (r1,g1,b1), (r2,g2,b2) in zip(lleft, lright)]
lBlueDiff  = [(0, 0, b1-b2) for (r1,g1,b1), (r2,g2,b2) in zip(lleft, lright)]
lTest  = [(0,0,0)] * len(lLDiff)
for i in range(len(lTest)):
    if lleft[i] != lright[i]:
        lTest[i] = lleft[i]

imLDiff.putdata(lLDiff)
imRDiff.putdata(lRDiff)
imAbsDiff.putdata(lAbsDiff)
imXor.putdata(lXor)
imRedDiff.putdata(lRedDiff)
imGreenDiff.putdata(lGreenDiff)
imBlueDiff.putdata(lBlueDiff)
imTest.putdata(lTest)

imLDiff.save("C:/leftdiff.jpg")
imRDiff.save("C:/rightdiff.jpg")
imAbsDiff.save("C:/absdiff.jpg")
imXor.save("C:/xor.jpg")
imRedDiff.save("C:/diffred.jpg")
imGreenDiff.save("C:/diffgreen.jpg")
imBlueDiff.save("C:/diffblue.jpg")
imTest.save("C:/testpic.jpg")
