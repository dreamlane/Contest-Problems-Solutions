# PermRLE.py
# Google Code Jam 2008 Round 2 Problem D: http://code.google.com/codejam/contest/32001/dashboard#s=p3&a=0
# Benjamin Johnson
# April 11 2012 10:38-11:15 small solved!
# Lessons Learned: 

import sys,math,time,itertools

filename = "PermRLE"

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

    # Solve problem... Large dataset too difficult
    k = int(inputFile.readline())
    S = inputFile.readline().strip()
    nums = []
    for i in xrange(0,k):
        nums.append(i)
    perms = itertools.permutations(nums)
    minsize = len(S)
    for perm in perms:
        newString = ""
        # apply the swap
        for i in range(0,len(S)/k):
            for j in range(0,k):
                newString += S[i*k+perm[j]]
        lastChar = None
        count = 0
        for char in newString:
            if char != lastChar:
                lastChar = char
                count += 1
        if count < minsize:
            minsize = count

    
        
    print minsize
    outputFile.write("%d"%minsize)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
