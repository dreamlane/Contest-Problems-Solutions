# Space.py
# Google Code Jam Round 1C 2011 Problem B: http://code.google.com/codejam/contest/1128486/dashboard
# Benjamin Johnson
# April 16 2012 9:17-9:37 stumped for now
# Lessons Learned:

import sys,math,time

filename = "Space"

inputFilename = filename+"-test.in"
#inputFilename = filename+"-small.in"
#inputFilename = filename+"-large.in"

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
    inputs = map(int,inputFile.readline().split())
    Boosters,timeToBuild,N,C = inputs[0],inputs[1],inputs[2],inputs[3]
    del inputs[0:4]
    distanceSequence = inputs
    starPath = []
    for i in xrange(0,N):
        starPath.append(distanceSequence[i%len(distanceSequence)])
            
    
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
