fname = "l2_ocr.txt"

d = {}
f = open(fname, "r")

for line in f:
    for c in line:
        d[c] = d.get(c, 0) + 1

for item in d.items():
    print item

print     

print [key for key in d.keys() if d[key] == 1]

f.close()
