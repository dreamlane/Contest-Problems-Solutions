# Cheating.py
# Google Code Jam 2008 Round 2 Problem A: http://code.google.com/codejam/contest/32001/dashboard
# Benjamin Johnson
# April 11 2012 10:06
# Lessons Learned: 

import sys,math,time

filename = "Cheating"

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
    M,V = map(int,inputFile.readline().split())
    nodes = []
    for iNode in range(0,(M-1)/2):
        nodes.append(map(int,inputFile.readline().split()))
    for lNode in range(0,(M+1)/2):
        nodes.append(int(inputFile.readline()))

    
        

    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
