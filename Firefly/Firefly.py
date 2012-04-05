# Firefly.py
# 2009 1C prob B 
# Benjamin Johnson
# March 8 2012 12:08-12:11 read prob, lunching, 2:44-4:08 stumped
# Lessons learned: There is a really simple vector math solution... learn more geometry

import sys
from math import sqrt
from numpy import dot

sys.setrecursionlimit(10000)

inputFile = open("Firefly-small.in","r") #Update these for the problem
outputFile = open("Firefly.txt","w") #

testcases = int(inputFile.readline())
for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    print "Case #",str(testcase+1)+": "

    # Solve problem...
    n = int(inputFile.readline())
    fireflies = []
    for i in range(n):
        fireflies.append(map(int,inputFile.readline().split()))
    
    #print fireflies
    # calculate the center of mass for 10 ticks 0-9 (helping me to solve the problem)
    # add up the total x,y,z then divide each by n
    '''
    for tick in range(10):
        cx = 0
        cy = 0
        cz = 0
        for x in range(n):
            ix = fireflies[x][0]
            cx += ix+(fireflies[x][3]*tick)
        for y in range(n):
            iy = fireflies[y][1]
            cy += iy+(fireflies[y][4]*tick)
        for z in range(n):
            iz = fireflies[z][2]
            cz += iz+(fireflies[z][5]*tick)
        cx = float(cx)/n
        cy = float(cy)/n
        cz = float(cz)/n
        print cx,cy,cz
        '''
    # Now i can see that the delta(cx,cy,cz) changes by the same amount every tick, because velocities don't change

    # Get the original center of mass, and then get the delta per tick
    cx = 0
    cy = 0
    cz = 0
    tick = 0
    for x in range(n):
        ix = fireflies[x][0]
        cx += ix+(fireflies[x][3]*tick)
    for y in range(n):
        iy = fireflies[y][1]
        cy += iy+(fireflies[y][4]*tick)
    for z in range(n):
        iz = fireflies[z][2]
        cz += iz+(fireflies[z][5]*tick)
    cx = float(cx)/n
    cy = float(cy)/n
    cz = float(cz)/n
    startCenter = (cx,cy,cz)

    delta = [0,0,0]
    for i in range(n):
        # add em all up
        delta[0] += fireflies[i][3]
        delta[1] += fireflies[i][4]
        delta[2] += fireflies[i][5]
    delta[0] = float(delta[0])/n
    delta[1] = float(delta[1])/n
    delta[2] = float(delta[2])/n

    #now we need to minimize the euclidean distance from (0,0,0)
    reference = (0,0,0)
    # solve for time
    time = 0.0
    num_1 = [0,0,0]
    num_2 = [0,0,0]
    denom = [0,0,0]
    for i in range(3):
        num_1[i] = startCenter[i]
        num_2[i] = delta[i]*100000
        denom[i] = abs(delta[i]*100000)**2

    numer = dot(num_1,num_2)
    time = -(numer/denom)
    print time
    
        
    

    
    outputDistance = "%1.8f "%distance
    outputTime = "%1.8f"%time
    outputString = outputDistance+outputTime
    
    outputFile.write(outputString)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

