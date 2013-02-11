##import xmlrpclib
##from xmlrpclib import Server

import urllib
##
##url = "http://www.pythonchallenge.com/pc/phonebook.php"
##server = Server(url)
##
##server.system.listMethods()
##
##print server.phone("Leopold")
##
leopoldUrl = "http://www.pythonchallenge.com/pc/stuff/violin.php"
u = urllib.urlopen(leopoldUrl)

text = u.read()
print text

u.close()
print u.headers
