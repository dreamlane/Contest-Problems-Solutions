# Centauri.py
# Google Code Jam EuroPython 2011 Problem A
# Benjamin Johnson
# March 13 2012
# Lessons Learned: 

import sys,math,string

filename = "Centauri"

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
    print "Case #",str(testcase+1)+": "

    # Solve problem...
    inputString = inputFile.readline().strip().lower()
    outputString = inputString.capitalize()+" is ruled by "
    outputFile.write(outputString)
    if inputString[-1] in "aeiou":
        outputFile.write("a queen.")
    elif inputString[-1] in "y":
        outputFile.write("nobody.")
    else:
        outputFile.write("a king.")
    
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

