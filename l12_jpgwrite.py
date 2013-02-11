f = open("C:/evil2.gfx", "rb")
s = f.read()
f.close()


for i in range(5):
    t = s[i::5]
    g = open("C:/evil2gfxmod%i.jpg" % i, "wb")
    g.write(t)
    g.close()
