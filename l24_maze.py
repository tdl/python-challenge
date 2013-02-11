from PIL import Image

im = Image.open("C:/maze.png")
width, height = im.size

print im.size, im.mode
print im.info

## maze will use sentinels in each direction
maze = [0] * width * height

l = list(im.getdata())

## loop all pixels, create maze
for i, p in enumerate(l):
    if p[:3] == (255, 255, 255): ## white pixels are paths
        maze[i] = 0
    else: ## the rest are walls
        maze[i] = 1

## last pixel on first row = start
start = width-1
assert maze[start] == 0
maze[start] = 2 
## first pixel on last row = finish
finish = height*width - width
assert maze[finish] == 0
maze[finish] = 3 


## put sentinels around maze!
swidth, sheight = width+2, height+2
mazeWithSentinels = [0] * swidth * sheight

## make first and last row all walls
mazeWithSentinels[0:swidth] = [1 for i in range(swidth)]
mazeWithSentinels[(sheight-1)*(swidth) : sheight*swidth] = [1 for i in range(swidth)]

## all other rows : make left and right edge walls
for i in range(1, sheight-1):
    mazeWithSentinels[i*swidth] = 1
    mazeWithSentinels[i*swidth + swidth - 1] = 1
    mazeWithSentinels[i*swidth+1 : i*swidth + swidth - 1] = \
                                 maze[(i-1)*width : (i-1)*width + width]

##for i in range(height):
##    print maze[i*width:i*width+width]

print
## discard original maze, use the one with sentinels now
maze = mazeWithSentinels
width, height = swidth, sheight

##for i in range(height):
##    print maze[i*width:i*width+width]

globalpos = (width + width - 2) ## go to start! (second-to-last pixel on row 2)
start = width + width - 2
assert maze[start] == 2
finish = (height-2) * width + 1
assert maze[finish] == 3

## exits will be a dict that maps a position to a list of 4 values :
## these values will indicate for N,E,S,W if there is an exit in that
## direction from this position
exits = {}

## lastTried will be a dict indicating from the given position in which direction
## we have last tried to walk
lastTried = {}

## track will be a list of the positions we've been so far (the route we follow)
## this will have to be popped when we backtrack
track = [globalpos]

def getExits(pos):
    ex = [0] * 4
    if maze[pos - width] in (0,3):
        ex[0] = 1 ## exit to north available
    if maze[pos + 1] in (0,3):
        ex[1] = 1 ## exit to east available
    if maze[pos + width] in (0,3):
        ex[2] = 1 ## exit to south available
    if maze[pos - 1] in (0,3):
        ex[3] = 1 ## exit to west available
    return ex

for y in range(1, height-1):
    for x in range(1, width-1):
        pos = y*width + x
        exits[pos] = getExits(pos)
        lastTried[pos] = -1

assert maze[globalpos] == 2

def N(pos):
    pos -= width
    return pos

def E(pos):
    pos += 1
    return pos

def S(pos):
    pos += width
    return pos

def W(pos):
    pos -= 1
    return pos

def showStats():
    print "pos = %d,%d" % (globalpos%width, globalpos/width)
    print "exits     :", exits[globalpos]
    print "track so far  :", [(pos%width, pos/width) for pos in track]
    print "lastTried here:", lastTried[globalpos]
 
moves = {0: N,  1: E,  2: S,  3: W}

imposs = False
## loop until we have found the finish
## OR until all routes from the current position are exhausted
cnt=0
while globalpos != finish:
    ##showStats()
    ## get an exit from here we haven't done yet
    trydir = lastTried.get(globalpos, -1) + 1
    while trydir < 4 and exits[globalpos][trydir] != 1 :
        trydir += 1
    if trydir > 3: ## no more exits from here we haven't tried! so backtrack
##        print "backtracking !!"
        ## go back to previous pos and shorten the route
        track.pop()
##        print "track so far  :", [(pos%width, pos/width) for pos in track]
        globalpos = track[-1]
        if (globalpos == start): ## check if we backtracked to the start
            imposs = True ## in that case the maze is unsolvable
            print "*** unsolvable maze !! ***"
            break
            
    else:
        ## try to move to chosen path
        newpos = moves[trydir](globalpos)
        lastTried[globalpos] += 1
        ## check if new position would be one we've already seen!!
        trrev = track[::-1]
        if newpos in trrev:
            ## don't go this way. next loop!
            continue
        else:
            globalpos = newpos
            track.append(globalpos)
##            print "track so far  :", [(pos%width, pos/width) for pos in track]
    cnt += 1
    if (cnt % 1000 == 0):
        print "loops done :", cnt, "track length:", len(track)

if len(track) < 100:
    print
    print "*** Solution :", [(pos%width, pos/width) for pos in track]
else :
    fo = open("C:/sol.txt")
    fo.writelines([str(t) for t in track])
    fo.close()
    

