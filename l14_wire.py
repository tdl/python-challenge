import PIL
from PIL import Image

f = Image.open("C:\\wire.png")
l = list(f.getdata())

lnew = []

## 100 is special case
cnt = 0
lnew.extend(l[cnt:cnt+100])
cnt += 100

for i in range(99, 0, -1):
    lnew.extend(l[cnt:cnt+i])
    cnt += i
    lnew.extend(l[cnt:cnt+i])
    cnt += i

print i
print cnt
print len(lnew)

g = Image.new("RGB", (100,100))
g.putdata(lnew)
g.save("C:\\aha.png")


lnew = []

## 100 is special case
cnt = 10000-1
lnew.extend(l[cnt:cnt-100:-1])
cnt -= 100

for i in range(99, 1, -1):
    lnew.extend(l[cnt:cnt-i:-1])
    cnt -= i
    lnew.extend(l[cnt:cnt-i:-1])
    cnt -= i

## now 1 is special too
lnew.extend(l[cnt::-1])
cnt -= 1

print i
print cnt
print len(lnew)

g = Image.new("RGB", (100,100))
g.putdata(lnew)
g.save("C:\\aha2.png")
