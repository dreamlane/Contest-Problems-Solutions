# ClosingTheLoop.py
# Google Code Jam 2011 Africa Qual problem 1
# Benjamin Johnson
# March 13 2012
# Lessons Learned: 

import sys,math

filename = "ClosingTheLoop"

#inputFilename = filename+"-test.in"
#inputFilename = filename+"-small.in"
inputFilename = filename+"-large.in"

outputFilename = filename+".txt"

inputFile = open(inputFilename,"r") #Update these for the problem
outputFile = open(outputFilename,"w") #

testcases = int(inputFile.readline())
for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    print "Case #",str(testcase+1)+": "

    # Solve problem...
    s = int(inputFile.readline())
    reds = []
    blues = []
    segments = inputFile.readline().split()
    for segment in segments:
        if segment[-1] == "R":
            reds.append(int(segment[0:-1]))
        else:
            blues.append(int(segment[0:-1]))

    blues.sort()
    blues.reverse()
    reds.sort()
    reds.reverse()
    length = 0
    lowest = min(len(blues),len(reds))
    for i in range(lowest):
        length += blues[i]-1
        length += reds[i]-1
    print length
    outputFile.write("%d"%length)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()
