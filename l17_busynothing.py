import urllib
import re

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
    u = urllib.urlopen(url)
    print 'url : %20s' % url.split("/")[-1],
    text = u.read()
    print 'text : %20s' % text,
    sHeaders = str(u.headers)
    cook = sHeaders.index("info=")
    endcook = sHeaders.index(";", cook)
    u.close()

    ckie = sHeaders[cook+5:endcook]
    ckiechars.append(ckie)
                      
    matches = re.findall(regex, text)

    if not matches:
        break
    else:
        m = matches[0]
        currval = m
        print 'new val = %s' % currval

print ckiechars
