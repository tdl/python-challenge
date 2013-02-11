def makenext(s):
    if len(s) < 1: return s

    s = s + "_" ## add a sentinel
    lastchar = s[0]
    cnt = 0
    new = []

    for pos in range(1, len(s)):
        cnt += 1
        c = s[pos]
        if c != lastchar:
            new.append(str(cnt))
            new.append(lastchar)
            cnt = 0
            lastchar = c
        pos += 1

    return "".join(new)

a = "1"
alist = [a]

for i in range(31):
    if len(a) < 70: 
        print "%d '%s' - len %d" % (i, a, len(a))
    else:
        print "%d '...' - len %d" % (i, len(a))
    a = makenext(a)
    alist.append(a)