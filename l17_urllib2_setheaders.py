import urllib, urllib2

url = "http://www.pythonchallenge.com/pc/stuff/violin.php"

txdata = None
txheaders = { 'Cookie': "info=" + urllib.quote_plus("the flowers are on their way") }
req = urllib2.Request(url, txdata, txheaders)
u = urllib2.urlopen(req)

headers = u.info()
print headers
data = u.read()
print data

u.close()
