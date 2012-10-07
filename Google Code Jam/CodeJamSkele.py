# CodeJamSkele.py
# Google Code Jam Skeleton
# Benjamin Johnson
# March 12 2012
# Lessons Learned: 

import sys,math,time

filename = ""

inputFilename = filename+"-test.in"
#inputFilename = filename+"-small.in"
#inputFilename = filename+"-large.in"

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

    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
