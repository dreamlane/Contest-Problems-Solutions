# Recyclable.py
# Google Code Jam 2012 Qual C
# Benjamin Johnson
# LIVE
# Lessons Learned: 

import sys,math,time

filename = "Recyclable"

#inputFilename = filename+"-test.in"
#inputFilename = filename+"-small.in"
inputFilename = filename+"-large.in"

outputFilename = filename+".txt"

inputFile = open(inputFilename,"r") #Update these for the problem
outputFile = open(outputFilename,"w") #

def isRecyclable(number,A,B,table):
    modifiers = []
    #if number in table:
        #return table[number]
    if number < 12:
        return 0
    ##if number/(10**(len(str(number))-1)) >= number%10:
        ##print "Number:",number,"'s first digit is greater than its last"
        ##print "first:",number/(10**(len(str(number))-1))
        ##print "last:",number%10
        ##return False
    for i in xrange(1,len(str(number))):
        modifiers.append((10**i,10**(len(str(number))-i)))

    ##print modifiers
    # Apply the modifiers and determine if the number is recyclable
    count = 0
    for modifier in modifiers:
        newNumber = (number/modifier[0])+(number%modifier[0])*modifier[1]
        if newNumber > number and newNumber <= B:
            table[(number,newNumber)] = 1
            #count += 1
    #if count > 0:
        #table[number] = count
    #return count

startTime = time.time()

testcases = int(inputFile.readline())
for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    print "Case #",str(testcase+1)+": "
    
    # Solve problem...
    table = {}
    count = 0
    A,B = map(int,inputFile.readline().split())
    for number in xrange(A,B):
        isRecyclable(number,A,B,table)
    count = len(table.keys())
    print count
    #sortedkeys = table.keys()
    #sortedkeys.sort()
    #for key in sortedkeys:
        #print key,table[key]
    outputFile.write("%d"%count)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
