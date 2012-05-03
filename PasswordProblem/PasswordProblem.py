# PasswordProblem.py
# Code Jam 2012 1A A: http://code.google.com/codejam/contest/1645485/dashboard 
# Benjamin Johnson
# May 3 2012 7:45-8:44 solved small, ran into precision error with large input, 9:59 issue solved by changing approach.
# Lessons Learned: When multiplying or dividing large numbers of decimals, consider precision.
#                   need to relearn the properties of logs.
#                   A little bit of paper math simplifies a solution...
#                   The commented parts below contain my solution, and the uncommented contain the simpler math solution

import sys,math,time
from decimal import *

filename = "PasswordProblem"

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

    # Solve problem... for each option, calculate the expected strokes, return the lowest number
    charsTyped, totalChars = map(int,inputFile.readline().split())
    probs = map(float,inputFile.readline().split())
    minimumStrokes = sys.maxint

    # Hitting enter right away
    enterStrokes = totalChars+2
    if enterStrokes < minimumStrokes:
        minimumStrokes = enterStrokes
    
    # Keep typing
    # Calculate the probability of typing it correct so far
    correctProb = 1
    for prob in probs:
        correctProb *= prob
    expected = totalChars-charsTyped+1+(totalChars+1)*(1-correctProb)
##    correctProb = Decimal(1)
##    correctExpected = 0
##    correctStrokes = totalChars-charsTyped+1
##    incorrectStrokes = correctStrokes+totalChars+1
##    for prob in probs:
##        correctProb *= Decimal(prob)
##    expected += correctStrokes*Decimal(correctProb)
##    expected += incorrectStrokes*(Decimal(1)-Decimal(correctProb))
    ##print expected, correctStrokes,incorrectStrokes,correctProb
    if expected < minimumStrokes:
        minimumStrokes = expected

    # pressing backspace
    # build a probabilities hash table
    probsTable = {}
    probsTable[charsTyped] = 1.0
    i = 0
    for deletes in range(charsTyped-1,-1,-1):
        probsTable[deletes] = probsTable[deletes+1]*probs[i]
        i+=1
    ##print probsTable
    deletes = 1
##    correctStrokes = (deletes*2)+totalChars-charsTyped+1
    while deletes<len(probs):
##        ##print "prob",correctProb
        expected = totalChars-charsTyped+(2*deletes)+1+(totalChars+1)*(1-probsTable[deletes])
##        incorrectStrokes = correctStrokes + totalChars + 1        
##        # get the expected value of this line
##        expected += correctStrokes*correctProb
##        expected += incorrectStrokes*(1-correctProb)
        if expected < minimumStrokes:
            minimumStrokes = expected
##        ##print expected,deletes
##        # Update data for next run
        deletes += 1
##        correctStrokes = (deletes*2)+totalChars-charsTyped+1
##        correctProb /= probs[-deletes]
    
    print minimumStrokes
    outputFile.write("%1.8f"%minimumStrokes)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
