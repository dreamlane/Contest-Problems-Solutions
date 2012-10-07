# TextMessage.py
# Solution to 2008 Round 1C A.
# Benjamin Johnson
# March 21 2012 Solved test case on the bus, worked for both large and small as well
# Lessons Learned: 

import sys,math,time
startTime = time.time()
filename = "TextMessage"

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
    #print "Case #",str(testcase+1)+": "

    # Solve problem...
    per_key, keys, letters = map(int,inputFile.readline().split())
    freqs = map(int,inputFile.readline().split())
    presses = {}
    for i in range(per_key):
        presses[i+1] = []
    least_presses = 1
    assign = 0
    freqs.sort()
    freqs.reverse()
    for letter in freqs:
        #assign the highest frequency values to a 1 press solution if possible
        #then assign the next ones to 2 presses and so forth
        #print letter
        if assign == keys:
            assign = 0
            least_presses+=1
        presses[least_presses].append(letter)
        assign+=1

    total = 0
    for presses_key in presses.keys():
        for letter in presses[presses_key]:
            total += letter*presses_key
            
    #print total
    #print presses
            
            
    
    outputFile.write("%d"%total)

    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()
print str(time.time()-startTime)
