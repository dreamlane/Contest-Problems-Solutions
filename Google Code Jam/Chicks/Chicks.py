# Chicks.py
# Google Code Jam Round 1B 2010 Problem B
# Benjamin Johnson
# March 12 2012 11:58-1:20  +2 failed small
# Lessons Learned: Sometimes, you need to rethink the strategy
#                  Make sure to understand the problem, and make sure the
#                  solution is the solution to the problem... I spent too much
#                  time minimizing the "time" elapsed, instead of the number of
#                  swaps.

import sys,math

filename = "Chicks"

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
    n,k,barn,time = map(int,inputFile.readline().split())

    starts = map(int,inputFile.readline().split())
    velocities = map(int,inputFile.readline().split())
    chicks = []
    for i in range(n):
        chicks.append([starts[i],velocities[i],None]) #[pos,vel,canmakeit]


    count = 0
    for i in range(len(chicks)):
        # determine if the chick can make it:
        x = chicks[i][0]
        v = chicks[i][1]
        if x+time*v < barn:
            chicks[i][2] = False
        else:
            chicks[i][2] = True
            count += 1
    
    # Get the number of passes
    passes = 0
    found = 0
    #print chicks
    if count < k:
        print "IMPOSSIBLE"
        outputFile.write("IMPOSSIBLE")
    else:
        for i in range(len(chicks)-1,-1,-1):
            #print "chick: " + str(chicks[i])
            if found == k:
                break
            if chicks[i][2]:
                found += 1
                for j in range(i+1,len(chicks)):
                    #print "sub-chick: "+str(chicks[j])
                    if not chicks[j][2]:
                        passes += 1
        print passes
        outputFile.write("%d"%passes)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

