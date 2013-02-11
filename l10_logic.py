def get_digit_count(c, s):
    cnt = 0
    x = s[cnt]

    while x == c:
        cnt += 1
        if (cnt == len(s)):
            break
        x = s[cnt]

##    print "c=", c, "cnt=", cnt
    return (c, str(cnt))

def makenext(s):
    cnt = 0
    next = ""
    while cnt < len(s):
        tup = get_digit_count(s[0], s)
        next = next + tup[1] + tup[0] ## add new count and digit
        cnt += int(tup[1])
        s = s[cnt:]
        cnt = 0
    return next

a = "1"
alist = [a]

for i in range(31):
    if len(a) < 70: 
        print "%d '%s' - len %d" % (i, a, len(a))
    else:
        print "%d '...' - len %d" % (i, len(a))
    a = makenext(a)
    alist.append(a)
    
