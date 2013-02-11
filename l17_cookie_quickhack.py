import urllib
import re
import bz2

def makeurl(base, param, value):
    return base + "?" + param + "=" + value

baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
param = "busynothing"
cnt = 300
currval = "12345"
regex = re.compile("(\d+)$")

getit = []

for i in range(cnt):
    url = makeurl(baseurl, param, currval)
    print "url :", str(url.split("/")[-1]).ljust(30),
    u = urllib.urlopen(url)
    text = u.read()
    headers = str(u.headers)
    cook = headers.index("info=")+5
    endcook = headers.index(";", cook)
    print "text :", text,
    print "cookie :", headers[cook:endcook]
    getit.append(headers[cook:endcook])

    try:
        text.index("ivide")
        newval = str(int(currval) / 2)
        print "** dividing by two !"
    except ValueError :
        newval = re.findall(regex, text)[0]

    currval = newval
    u.close()
                       
print getit
this = urllib.unquote_plus("".join(getit))
print bz2.decompress(this)

