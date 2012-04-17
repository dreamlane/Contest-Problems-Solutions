# SquareTiles.py
# Google Code Jam Round 1C 2011 Problem A: http://code.google.com/codejam/contest/1128486/dashboard
# Benjamin Johnson
# April 16 2012
# Lessons Learned: To write a '/' to a string in python you need to use '//'

import sys,math,time

filename = "SquareTiles"

#inputFilename = filename+"-test.in"
#inputFilename = filename+"-small.in"
inputFilename = filename+"-large.in"

outputFilename = filename+".txt"

inputFile = open(inputFilename,"r") #Update these for the problem
outputFile = open(outputFilename,"w") #

startTime = time.time()

testcases = int(inputFile.readline())
for testcase in xrange(0,testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    print "Case #",str(testcase+1)+": "

    # Solve problem...
    R,C = map(int,inputFile.readline().split())
    tiles = []
    impossible = False
    for i in xrange(0,R):
        row = list(inputFile.readline().strip())
        tiles.append(row)

    for row in xrange(0,R):
        for column in xrange(0,C):
            if tiles[row][column] == "#":
                tiles[row][column] = "/"
                if row < R-1: #Make sure we're not on the last row
                    if tiles[row+1][column] == "#":
                        tiles[row+1][column] = "\\"
                    else:
                        impossible = True
                    if column < C-1: #Make sure we're not in the bottom right corner
                        if tiles[row+1][column+1] == "#":
                            tiles[row+1][column+1] = "/"
                        else:
                            impossible = True
                    else:
                        impossible = True
                else:
                    impossible = True
                if column < C-1: #Make sure we're not on the far right
                    if tiles[row][column+1] == "#":
                        tiles[row][column+1] = '\\'
                    else:
                        impossible = True
                else:
                    impossible = True

    outputFile.write("\n")
    if impossible:
        print "Impossible"
        outputFile.write("Impossible\n")
    else:
        for row in tiles:
            for column in row:
                sys.stdout.write("%s"%column)
                outputFile.write("%s"%column)
            sys.stdout.write("\n")
            outputFile.write("\n")
                    
    
        

    # Output a new line for the next problem
    #outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
