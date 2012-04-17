# Dancing.py
# Google Code Jam 2012 Qual B
# Benjamin Johnson
# LIVE
# Lessons Learned: 

import sys,math,time

filename = "Dancing"

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

    # Solve problem...
    inputs = map(int,inputFile.readline().split())
    N = inputs[0]
    S = inputs[1]
    p = inputs[2]
    del inputs[0:3]
    
    # sort the list in decending order
    inputs.sort()
    inputs.reverse()

    # build the list of safe scores
    scores = []
    for totalS in inputs:
        base = totalS/3
        remain = totalS%3
        
        judges = []
        for i in range (0,3):
            if remain > 0:
                judges.append(base+1)
                remain -= 1
            else:
                judges.append(base)
        scores.append(judges)
    print inputs
    print scores
    print len(scores)
    print "---"

    #Remove all score sets that have max >= p
    count = 0
    scoresCopy = scores[:]
    for score in scoresCopy:
        if max(score) >= p:
            count += 1
            scores.remove(score)
        else:
            break
    print count
    print scores
    print len(scores)

    #Now maximize the max(score) for all the specials
    i = 0
    while S > 0 and i < len(scores):
        base = sum(scores[i])/3
        remain = sum(scores[i])%3
        if (remain == 0 or remain == 1) and base != 0:
            if base+1 >= p:
                count += 1
                S -= 1
                i += 1
            else:
                i += 1
        elif base != 0:
            if base+2 >= p:
                count += 1
                S -= 1
                i += 1
            else:
                i += 1
        else: # A zero base
            print "zero base, not a possible maxxer"
            i += 1
    print count
    outputFile.write("%d"%count)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
