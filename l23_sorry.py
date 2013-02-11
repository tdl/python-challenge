import xmlrpclib
from xmlrpclib import ServerProxy

server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print server.system.listMethods()

print server.phone("Leopold")
print server.phone("leopold")
print server.phone("sorry")
print server.phone("please")
print server.phone("please!")
