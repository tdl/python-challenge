import difflib
from difflib import Differ

def writeToFile(fNameOut, aList):
    """ Little helper to write a list of strings to a file,
        with correct closing of the file too.
    """
    fo = open(fNameOut, "w")
    fo.writelines(aList)
    fo.close()


fn = "C:/delta.txt"
f = open(fn, "r")
left, right = [], []
# split "deltas" file into a left and right part
for line in f:
    line = line.rstrip("\n")
    left.append(line[:53] + "\n")
    right.append(line[56:] + "\n")
f.close()

writeToFile("C:/left.txt", left)
writeToFile("C:/right.txt", right)

d = Differ()
result = list(d.compare(left, right))

writeToFile("C:/diff.txt", result)

newleft, newright, newall = [], [], []

for line in result:
    ## write to left only lines that are in left!
    if line[0] == "-":
        newleft.append(line[2:])
    ## write to right only lines that are in right!
    elif line[0] == "+":
        newright.append(line[2:])
    ## write to "all" lines that are in both sides!
    else:
        newall.append(line[2:])        
        
def convHexTxtToBytesFile(fnameIn, fnameOut):
    hexlist = []
    fi = open(fnameIn)
    for line in fi:
        line = line.rstrip("\n")
        hexlist.extend(line.split())
    fi.close()

    fo = open(fnameOut, "wb")
    charList = [chr(int(cHex, 16)) for cHex in hexlist]
    fo.writelines(charList)
    fo.close()

writeToFile("C:/in_left.txt", newleft)
writeToFile("C:/in_right.txt", newright)
writeToFile("C:/in_all.txt", newall)

convHexTxtToBytesFile("C:/in_left.txt", "C:/out_left.png")
convHexTxtToBytesFile("C:/in_right.txt", "C:/out_right.png")
convHexTxtToBytesFile("C:/in_all.txt", "C:/out_all.png")
