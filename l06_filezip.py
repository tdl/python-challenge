import re, zipfile

zfilename = "l6_channel.zip"
currval = "90052"
regex = re.compile("([0-9]+$)")
zipcomments = []

zfile = zipfile.ZipFile(zfilename)

while True:
    fname = currval + ".txt"
##    print "file : %s" % fname,  
    text = zfile.read(fname)
##    print ("text : %s" % text).ljust(30),
    ## get zip-comment of the file we're dealing with now
    inf = zfile.getinfo(fname)
##    print "zipcomment : '%s'" % inf.comment
    zipcomments.append(inf.comment)

    matches = re.findall(regex, text)
    if not matches:
        break
    currval = matches[0]

print "".join(zipcomments)
                       
    

