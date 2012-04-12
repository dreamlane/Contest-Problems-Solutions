# OddManOut.py
# Google Code Jam Solution to problem A from 2011 Africa: http://code.google.com/codejam/contest/438101/dashboard
# Benjamin Johnson
# April 12 2012 10:50
# Lessons Learned: 

import sys,math,time

filename = "OddManOut"

#inputFilename = filename+"-test.in"
#inputFilename = filename+"-small.in"
inputFilename = filename+"-large.in"

outputFilename = filename+".txt"

inputFile = open(inputFilename,"r") #Update these for the problem
outputFile = open(outputFilename,"w") #

startTime = time.time()

testcases = int(inputFile.readline())
for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    print "Case #",str(testcase+1)+": "

    # Solve problem...
    G = int(inputFile.readline())
    codes = map(int,inputFile.readline().split())
    codeTable = {}
    solos = {}
    for code in codes:
        if code in codeTable:
            if code in solos:
                del solos[code]
        else: # code seen only once
            codeTable[code] = None
            solos[code] = None
    print solos.keys()[0]
    outputFile.write("%d"%solos.keys()[0])
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
