# AirportWalkways.py
# Google Code Jam Round 2 2011
# Benjamin Johnson
# March 13 2012 5:00-6:38,11:03-11:41 3 failed small submissions
# Lessons Learned: Don't oversimplify the problem... If the problem spends
#                  a huge chunk of time describing a desicion that needs to be
#                  made, don't arbitrarily disregard that choice and say run all of the time.

import sys,math

filename = "AirportWalkways"

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
    length,walk,run,energy,count = map(int,inputFile.readline().split())
    walkways = []
    hall = []
    for walkway in range(count):
        walkways.append(map(int,inputFile.readline().split()))
    # create 0-speed walkways in between the real walkways
    if walkways[0][0] == 0:
        hall.append(walkways[0])
    else:
        newWalk = [0,walkways[0][0],0]
        hall.append(newWalk)
        hall.append(walkways[0])
    for i in range(1,count):
        if walkways[i][0] == walkways[i-1][1]:
            hall.append(walkways[i])
        else:
            newWalk = [walkways[i-1][1],walkways[i][0],0]
            hall.append(newWalk)
            hall.append(walkways[i])
    if hall[-1][1] != length:
        hall.append([hall[-1][1],length,0])

    # sort the segments by speed in ascending order
    hall.sort(key=lambda x: x[2])
    #print length,walk,run,energy
    #print hall
    #print hall
    total = 0
    energyLeft = energy
    for segment in hall:
        if energyLeft > 0:
            #print "Running segment: "+str(segment)
            segmentTime = float(segment[1]-segment[0])/(run+segment[2])
            #print segmentTime
            if segmentTime > energyLeft:
                
                # replace the segment with 2 new segments and calculate the time
                # taken to go through them
                distanceRan = (run+segment[2])*energyLeft
                energyLeft = 0
                segmentRan = [segment[0],segment[0]+distanceRan,run+segment[2]]
                segmentWalked = [segmentRan[1],segment[1],walk+segment[2]]
                #print "not enough energy: "+str(segmentRan+segmentWalked)
                total += float(segmentRan[1]-segmentRan[0])/(segmentRan[2])
                total += float(segmentWalked[1]-segmentWalked[0])/(segmentWalked[2])
                #print (float(segmentRan[1]-segmentRan[0])/(segmentRan[2]))
                #print (float(segmentWalked[1]-segmentWalked[0])/(segmentWalked[2]))
            else:
                energyLeft -= segmentTime
                total += segmentTime
        else:
            total += float(segment[1]-segment[0])/(walk+segment[2])

    print total
    outputFile.write("%1.8f"%total)

    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

