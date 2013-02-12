import urllib
import pickle

baseurl = "http://www.pythonchallenge.com/pc/def/banner.p"

reader = pickle.load(urllib.urlopen(baseurl))

textlist = []

for line in reader:
    textlist.extend([char * cnt for char, cnt in line]) 
    textlist.append("\n")

print "".join(textlist)
