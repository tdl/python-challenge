import PIL
from PIL import Image

fn = "C:/balloons.jpg"
im = Image.open(fn)
width, height = im.size

imData = list(im.getdata())

lleft = []
lright = []

for y in range(height):
    lleft.extend(imData[y*width : y*width + width/2])
    lright.extend(imData[y*width + width/2 : y*width + width])

def tup_add(p1, p2):
    r1,g1,b1 = p1
    r2,g2,b2 = p2
    return (r1+r2, g1+g2, b1+b2)

def tup_sub_l(p1, p2):
    r1,g1,b1 = p1
    r2,g2,b2 = p2
    return (r1-r2, g1-g2, b1-b2)

def tup_sub_r(p1, p2):
    r1,g1,b1 = p1
    r2,g2,b2 = p2
    return (r2-r1, g2-g1, b2-b1)

def tup_sub_abs(p1, p2):
    r1,g1,b1 = p1
    r2,g2,b2 = p2
    return (abs(r1-r2), abs(g1-g2), abs(b1-b2))

def tup_xor(p1, p2):
    r1,g1,b1 = p1
    r2,g2,b2 = p2
    return (r1^r2, g1^g2, b1^b2)

def tup_and(p1, p2):
    r1,g1,b1 = p1
    r2,g2,b2 = p2
    return (r1&r2, g1&g2, b1&b2)

def tup_or(p1, p2):
    r1,g1,b1 = p1
    r2,g2,b2 = p2
    return (r1|r2, g1|g2, b1|b2)

def tup_avg(p1, p2):
    r1,g1,b1 = p1
    r2,g2,b2 = p2
    return ((r1+r2)/2, (g1+g2)/2, (b1+b2)/2)

def tup_sub_l_red(p1, p2):
    r1,g1,b1 = p1
    r2,g2,b2 = p2
    return (r1-r2,0,0)

def tup_sub_l_green(p1, p2):
    r1,g1,b1 = p1
    r2,g2,b2 = p2
    return (0,g1-g2,0)

def tup_sub_l_blue(p1, p2):
    r1,g1,b1 = p1
    r2,g2,b2 = p2
    return (0,0,b1-b2)

funcs = [tup_add, tup_sub_l, tup_sub_r, tup_sub_abs, tup_xor, \
         tup_and, tup_or, tup_avg, \
         tup_sub_l_red, tup_sub_l_green, tup_sub_l_blue]
nrTypes = len(funcs)

newsize = (width/2, height)
images = [Image.new("RGB", newsize) for i in range(nrTypes)]
lists = [[0] * len(lleft) for i in range(nrTypes)]

## walk through pixels of left and right images
for i, p in enumerate(zip(lleft, lright)):
    ## for each pixel : perform each operation (add, sub, xor, ...)
    ## and store in corresponding result list
    for f, currlist in zip(funcs, lists):
        currlist[i] = f(p[0], p[1])

for i in range(len(images)):
    images[i].putdata(lists[i])
    images[i].save("C:/im_" + funcs[i].func_name + ".jpg")

