import xmlrpclib
from xmlrpclib import ServerProxy

server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print server.system.listMethods()

##we zien nu dat er een "phone" method is.

print server.phone("bert")
print server.phone("Bert")
print server.phone("BERT")

##enkel "Bert" werkt.

