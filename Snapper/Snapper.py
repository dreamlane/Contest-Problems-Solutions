# Snapper.py
# Google Code Jam 2010 Qual
# Benjamin Johnson
# March 14 2012 9:33 
# Lessons Learned: 

import sys,math

filename = "Snapper"

#inputFilename = filename+"-test.in"
inputFilename = filename+"-small.in"
#inputFilename = filename+"-large.in"

outputFilename = filename+".txt"

inputFile = open(inputFilename,"r") #Update these for the problem
outputFile = open(outputFilename,"w") #

testcases = int(inputFile.readline())
for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    #print "Case #",str(testcase+1)+": "

    # Solve problem...
    n,k = map(int,inputFile.readline().split())
    if n <= len(bin(k))-2:
        #print n,k
        bits = bin(k)[::-1]
        bits = bits[0:-2]
        print n
        print bits
        if bits[n-1] == "0":
            #print "OFF"
            outputFile.write("OFF")
            print "off"
        else:
            #print "ON"
            outputFile.write("ON")
            print "on"
    else:
        print n,k
        print "OFF"
        outputFile.write("OFF")
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

