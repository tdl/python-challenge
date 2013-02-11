import PIL
from PIL import Image

f = Image.open("C:\\wire.png")
l = list(f.getdata())

lnew = []
pos = 0

## 100 is special case
for j in range(100):
    lnew.append(l[pos + 100*j])
pos += 1

for i in range(99, 0, -1):
    for j in range(i):
        lnew.append(l[pos + i*j])
    pos += 1
    for j in range(i):
        lnew.append(l[pos + i*j])

print pos
print len(lnew)

g = Image.new("RGB", (100,101))
g.putdata(lnew)
g.save("C:\\kijknu!!.png")


