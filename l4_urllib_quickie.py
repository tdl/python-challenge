import urllib
import re

def makeurl(base, param, value):
    return base + "?" + param + "=" + value

baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
param = "nothing"
cnt = 300
currval = "12345"
regex = re.compile("(\d+)$")

for i in range(cnt):
    url = makeurl(baseurl, param, currval)
    print "url :", str(url.split("/")[-1]).ljust(30),
    u = urllib.urlopen(url)
    text = u.read()
    print "text :", text

    try:
        text.index("ivide")
        newval = str(int(currval) / 2)
        print "** dividing by two !"
    except ValueError :
        newval = re.findall(regex, text)[0]

    currval = newval
    u.close()
