import urllib, cStringIO
from PIL import Image

s = "http://www.pythonchallenge.com/pc/def/oxygen.png" ## url of image
u = urllib.urlopen(s)
content = u.read()
u.close()

filelike = cStringIO.StringIO(content)
im = Image.open(filelike)
print im.size, im.mode
w, h = im.size

l = list(im.getdata())
## start "reading" left to right about halfway down the image
chars = [l[(h/2)*w + i] for i in range(0, w, 7)]
print "".join([chr(c[0]) for c in chars])
