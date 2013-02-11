import urllib, urllib2, base64, re
from urllib2 import HTTPError

url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"

txdata = None
txheaders = {
              'Range': 'bytes=30203-',
              'Authorization': 'Basic ' + base64.encodestring("butter:fly")
            }
##txheaders['Range'] = 'bytes 30203-60405/2123456789'

##iets = urllib.urlopen(url)
##print iets.headers
##iets.close()

regex   = re.compile("Content-Range: bytes [0-9]+-([0-9]+)")
regexSt = re.compile("Content-Range: bytes ([0-9]+)-[0-9]+")
val, val2 = 30203, 2123456789

for i in 0,1:
## we wanna loop twice : first go forward from 30203 (i==0),
## then go backward from 2123456789 (when i==1)
    if i==0: 
        theval = val
        theregex = regex
        add = 1
    else:
        theval = val2
        theregex = regexSt
        add = -1

    while True:

        txheaders['Range'] = 'bytes=%d-' % theval
           
        print txheaders

        try:
            req = urllib2.Request(url, txdata, txheaders)
            u = urllib2.urlopen(req)
            print u.read()
        except HTTPError, ex:
            print "Exception --- response code", ex.code, "--- headers were :"
            if ex.code == 206: ## "partial content" response
                print ex.headers
                matches = re.findall(theregex, str(ex.headers))
                if not matches:
                    break
                match = matches[0]
                theval = int(match) + add
            else:
                break ## quit it !
            print "read :", ex.read(), "new val :", theval

print "*** done part 1 ***"        


## now go again but save all data we encounter !
data = []
val = 1152983631
theval = val
theregex = regex
add = 1

while True:

    txheaders['Range'] = 'bytes=%d-' % theval
       
    print txheaders

    try:
        req = urllib2.Request(url, txdata, txheaders)
        u = urllib2.urlopen(req)
        print u.read()
    except HTTPError, ex:
        print "Exception --- response code", ex.code, "--- response headers :"
        if ex.code == 206: ## "partial content" response
            print ex.headers
            matches = re.findall(theregex, str(ex.headers))
            if not matches:
                break
            match = matches[0]
            theval = int(match) + add
        else:
            break ## quit it !

        data.append(ex.read())
        print "read :", data[-1], "new val :", theval

print "*** done part 2 ***"        

print len(data)
fo = open("C:/aha!.zip", "wb")
fo.writelines(data)
fo.close()

print "*** done part 3 (wrote zip file) ***"        
