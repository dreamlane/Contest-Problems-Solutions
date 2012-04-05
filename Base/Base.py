# Base.py
# 2009 1C prob C
# Benjamin Johnson
# March 8 2012 11:28-12:05 + one wrong submission on small... score: 41
# Lessons learned: Always double check "=" vs "=="

import sys

sys.setrecursionlimit(10000)

inputFile = open("Base-large.in","r") #Update these for the problem
outputFile = open("Base.txt","w") #

testcases = int(inputFile.readline())
for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    print "Case #",str(testcase+1)+": "

    # Solve problem...
    inputString = inputFile.readline().strip()
    uniqueChars = []
    for char in inputString:
        if char not in uniqueChars:
            uniqueChars.append(char)
    #The chars are added in the order that they are found
    base = len(uniqueChars)
    # can't be unary
    if base == 1:
        base = 2

    # determine the best possible mapping of chars to values
    # with the longest string being 61, we can brute force it
    # I anticipate that the correct arrangment of values will be [1,0,2,3,4...,base-1]
    values = [1,0]
    if base > 2:
        for i in range(2,base):
            values.append(i)
    chars = {}
    for i in range(len(uniqueChars)):
        chars[uniqueChars[i]] = values[i]
    # now the chars are mapped to their values
    print chars
    # calculate the minimum time
    time = 0
    for i in range(len(inputString)):
        charValue = chars[inputString[i]]
        time += charValue*base**(len(inputString)-i-1)
    print time
    outputFile.write("%d"%time)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

