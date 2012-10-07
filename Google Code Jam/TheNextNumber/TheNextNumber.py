# TheNextNumber.py
# Google Code Jam Round 1B 2009 B: http://code.google.com/codejam/contest/186264/dashboard#s=p1
# Benjamin Johnson
# April 26 2012 8:55-9:55 solved small, 10:00 - 11:25 solved large
# Lessons Learned: Sometimes an algorithm can be discovered...
# ... by analyzing the inputs and outputs of a bruteforce algorithm that works

import sys,math,time,itertools

filename = "TheNextNumber"

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

    # Solve problem... Not sure how to go about solving the large input, but the small input is trivial
    # ... Update: After thinking about it for awhile and comparing the small input and output
    # ... I've come up with the following algorithm:
    # From the leftmost digits to the right:
    #     Test to see if the digit can swap with a digit to its left:
    #        A digit can only swap if the other digit is smaller
    #     Then sort the digits that were to the right of the digit that was swapped
    #     If no swaps occured and all digit positions where checked, then add a "0" to the front of the number.
    #     Then do the algorithm again
    #
    #   NOTE there is a special condition that must be satisfied...
    # ..... We want to swap at the highest possible leftIndex value
    N = inputFile.readline().strip()

    # OLD CODE USED TO SOLVE THE SMALL INPUT
##    setOfNumbers = set()
##    for perm in itertools.permutations(N):
##        if int("".join(perm)) > int(N):
##            if setOfNumbers:
##                if int("".join(perm)) < min(setOfNumbers):
##                    setOfNumbers.add(int("".join(perm)))
##            else:
##                setOfNumbers.add(int("".join(perm)))
##    print setOfNumbers
##    if not setOfNumbers:
##        for perm in itertools.permutations("0"+N):
##            if int("".join(perm)) > int(N):
##                if setOfNumbers:
##                    if int("".join(perm)) < min(setOfNumbers):
##                        setOfNumbers.add(int("".join(perm)))
##                else:
##                    setOfNumbers.add(int("".join(perm)))
##    setOfNumbers = list(setOfNumbers)
##    setOfNumbers.sort()
##    print setOfNumbers[0]
##    
##    outputFile.write("%d"%setOfNumbers[0])
    rightIndex = len(N)-1
    swapFound = False
    outputString = ""
    highestLeft = -sys.maxint
    solutionRightIndex = 0
    while not swapFound or rightIndex > 0:
        if rightIndex > 0:
            for leftIndex in range(rightIndex-1,-1,-1):
                ##print leftIndex,rightIndex
                ##print int(N[leftIndex]),int(N[rightIndex])
                if int(N[leftIndex]) < int(N[rightIndex]):
                    # Check for swap optimality
                    ##print leftIndex,highestLeft
                    if leftIndex > highestLeft:
                        highestLeft = leftIndex
                        solutionRightIndex = rightIndex
                        swapFound = True
                        ##print highestLeft,solutionRightIndex,N
            rightIndex-=1
        else:
            N = "0"+N
            rightIndex = len(N)-1
            highestLeft = -sys.maxint
            solutionRightIndex = 0
    ##print "Swapping pos:",solutionRightIndex,"with pos:",highestLeft
    charList = list(N)
    charList[highestLeft],charList[solutionRightIndex] = charList[solutionRightIndex],charList[highestLeft]
    if highestLeft < len(N)-2: #Then we need to sort the digits to the right
        ##print "sorting digits to the right of pos:",highestLeft
        intList = map(int,charList)
        intList[highestLeft+1:] = sorted(intList[highestLeft+1:])
        N = "".join(map(str,intList))
    else:
        N = "".join(charList)
    print N
    outputString = "".join(N)
    outputFile.write(outputString)            
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
