# CrossingTheRoad.py
# Google Code Jam 2009 1A B: http://code.google.com/codejam/contest/188266/dashboard#s=p1
# Benjamin Johnson
# April 24 2012 9:56-12:15 solved small! It runs very fast for the large, but there is a bug, so my submission is wrong
# Lessons Learned: 

import sys,math,time
from heapq import *

filename = "CrossingTheRoad"

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

    # Solve problem... Only attempting the small input
    # If we get all possible paths (ignoring back tracking),
    # ... we can build a tree the represents all reasonable paths,
    # ... and then take the leaf node with the minimum cost
    # The tree would have at most 3^12 nodes, but most likely will have
    # ... no more than 2^10.
    # ... The realization of this is the AI search algorithm Uniform Cost

    # Get the inputs
    N,M = map(int,inputFile.readline().split())
    inputs = []
    for i in xrange(N):
        inputs.append(map(int,inputFile.readline().split()))
    # Normalize the intersections
    intersections = []
    for x in xrange(N):
        row = []
        for y in xrange(M):
            row.append(inputs[-(x+1)][y*3:y*3+3])
        intersections.append(row)
    #print intersections
    
    solution = None
    # perform a uniform cost search of the graph, where the graph is created as we search
    # start with the node at 0,0, NOTE y,x
    corner = (0,(0,0))
    frontier = [corner]
    frontierKeys = {}
    frontierKeys[corner[1]] = corner[0]
    explored = {}
    goalCorner = (N*2-1,M*2-1)
    #print goalCorner
    while frontier:
        #print frontier
        #Get the lowest cost node in the frontier
        corner = heappop(frontier)
        #Check to see if this corner is our goal
        if corner[1] == goalCorner:
            print "found goal corner:"
            print corner[0]
            solution = corner[0]
            break
        # Add this corner to explored
        explored[corner[1]] = None
        
        # Expand the options by adding them to the frontier
        
        # Up
        # Make sure up is on the board and not already explored
        up = (corner[1][0]+1,corner[1][1])
        if up[0] < N*2 and up not in explored:
            # Calculate the cost of the move
            cost = corner[0]
            # Are we crossing green or intersection?
            if up[0]%2 == 0:
                #crossing green
                cost += 2
            else:
                #crossing intersection
                #The time to cross an intersection = 1+timeToGreen
                #timeToGreen = nextGreen-currentTime if it's not green now
                T = intersections[up[0]/2][up[1]/2][2]
                S = intersections[up[0]/2][up[1]/2][0]
                W = intersections[up[0]/2][up[1]/2][1]
                patternPosition = cost-T
                if patternPosition%(S+W) >= S:
                    #then it's off, lets get the time to turn
                    timeToGreen = (S+W)-patternPosition%(S+W)
                    cost += 1+timeToGreen
                    ##print timeToGreen
                else:
                    ##print "up is green"
                    #then it's on
                    cost += 1
            # Check to see if it is in Frontier
            if up in frontierKeys:
                # Check to see if this new path is faster
                if frontierKeys[up] > cost:
                    # if it is, replace the old one
                    frontier.remove((frontierKeys[up],up))
                    heappush(frontier,(cost,up))
                    frontierKeys[up] = cost
            else:
                frontierKeys[up] = cost
                heappush(frontier,(cost,up))

        # Right
        # Make sure right is on the board and not already explored
        right = (corner[1][0],corner[1][1]+1)
        if right[1] < M*2 and right not in explored:
            # Calculate the cost of the move
            cost = corner[0]
            # Are we crossing green or intersection?
            if right[1]%2 == 0:
                #crossing green
                cost += 2
            else:
                #crossing intersection
                #The time to cross an intersection = 1+timeToGreen
                #timeToGreen = nextGreen-currentTime if it's not green now
                T = intersections[right[0]/2][right[1]/2][2]
                S = intersections[right[0]/2][right[1]/2][0]
                W = intersections[right[0]/2][right[1]/2][1]
                ##print right
                ##print T
                ##print S
                ##print W
                patternPosition = cost-T
                if patternPosition%(S+W) < S :
                    #then it's off, lets get the time to turn
                    timeToGreen = S-patternPosition%(S+W)
                    cost += 1+timeToGreen
                    ##print timeToGreen
                else:
                    ##print "up is green"
                    #then it's on
                    cost += 1
            # Check to see if it is in Frontier
            if right in frontierKeys:
                ##print right,"in frontier already with cost:",frontierKeys[right]
                ##print "new cost:",cost
                # Check to see if this new path is faster
                if frontierKeys[right] > cost:
                    ##print "replacing",right
                    # if it is, replace the old one
                    frontier.remove((frontierKeys[right],right))
                    heappush(frontier,(cost,right))
                    frontierKeys[right] = cost
            else:
                frontierKeys[right] = cost
                heappush(frontier,(cost,right))
        # Down
        # Make sure right is on the board and not already explored
        down = (corner[1][0]-1,corner[1][1])
        if down[0] >= 0 and down not in explored:
            # Calculate the cost of the move
            cost = corner[0]
            # Are we crossing green or intersection?
            if down[0]%2 != 0:
                #crossing green
                cost += 2
            else:
                #crossing intersection
                #The time to cross an intersection = 1+timeToGreen
                #timeToGreen = nextGreen-currentTime if it's not green now
                T = intersections[down[0]/2][down[1]/2][2]
                S = intersections[down[0]/2][down[1]/2][0]
                W = intersections[down[0]/2][down[1]/2][1]
                patternPosition = cost-T
                if patternPosition%(S+W) > S:
                    #then it's off, lets get the time to turn
                    timeToGreen = (S+W)-patternPosition%(S+W)
                    cost += 1+timeToGreen
                    ##print timeToGreen
                else:
                    ##print "down is green"
                    #then it's on
                    cost += 1
            # Check to see if it is in Frontier
            if down in frontierKeys:
                # Check to see if this new path is faster
                if frontierKeys[down] > cost:
                    # if it is, replace the old one
                    frontier.remove((frontierKeys[down],down))
                    heappush(frontier,(cost,down))
                    frontierKeys[down] = cost
            else:
                frontierKeys[down] = cost
                heappush(frontier,(cost,down))
        # Left
        # Make sure right is on the board and not already explored
        left = (corner[1][0],corner[1][1]-1)
        if left[1] >= 0 and left not in explored:
            # Calculate the cost of the move
            cost = corner[0]
            # Are we crossing green or intersection?
            if left[1]%2 != 0:
                #crossing green
                cost += 2
            else:
                #crossing intersection
                #The time to cross an intersection = 1+timeToGreen
                #timeToGreen = nextGreen-currentTime if it's not green now
                T = intersections[left[0]/2][left[1]/2][2]
                S = intersections[left[0]/2][left[1]/2][0]
                W = intersections[left[0]/2][left[1]/2][1]
                patternPosition = cost-T
                if patternPosition%(S+W) < S :
                    #then it's off, lets get the time to turn
                    timeToGreen = S-patternPosition%(S+W)
                    cost += 1+timeToGreen
                    ##print timeToGreen
                else:
                    ##print "up is green"
                    #then it's on
                    cost += 1
            # Check to see if it is in Frontier
            if left in frontierKeys:
                # Check to see if this new path is faster
                if frontierKeys[left] > cost:
                    # if it is, replace the old one
                    frontier.remove((frontierKeys[left],left))
                    heappush(frontier,(cost,left))
                    frontierKeys[left] = cost
            else:
                frontierKeys[left] = cost
                heappush(frontier,(cost,left))
            
    outputFile.write("%d"%solution)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
