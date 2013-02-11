import urllib
import re
import bz2

base = ("http://www.pythonchallenge.com/pc/def/linkedlist.php")
param = "busynothing"
currval = "12345"

def makeUrl(base, param, val):
    return base + "?" + param + "=" + str(val)

regex = re.compile("([0-9]+$)")

ckiechars = []

while True:
    ## find "nothing"'s
    url = makeUrl(base, param, currval)
    resp = urllib.urlopen(url)
    print 'url : %32s' % url.split("/")[-1],

    text = resp.read()
    print 'text : %35s' % text,

    respheaders = resp.info()
    cookie = resp.info().getheader('Set-Cookie')
    cookB = cookie.index("info=")
    cookE = cookie.index(";", cookB)
    ckievalue = cookie[cookB+5:cookE]
    print 'cookie : %3s' % ckievalue,

    ckiechars.append(ckievalue)

    resp.close()
                      
    matches = re.findall(regex, text)

    if not matches:
        break
    else:
        m = matches[0]
        currval = m
        print 'new val = %s' % currval

print
print ckiechars
print "".join(ckiechars)
print urllib.unquote_plus("".join(ckiechars))
print bz2.decompress(urllib.unquote_plus("".join(ckiechars)))
