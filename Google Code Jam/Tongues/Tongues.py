# Tongues.py
# Google Code Jam 2012 Qual A
# Benjamin Johnson
# LIVE
# Lessons Learned: 

import sys,math,time

filename = "Tongues"

#inputFilename = filename+"-test.in"
inputFilename = filename+"-small.in"
#inputFilename = filename+"-large.in"

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
    inputString = inputFile.readline().strip()
    outputString = ""
    # the old fashioned if statement way
    for char in inputString:
        if char == "a":
            outputString += "y"
        elif char == "b":
            outputString += "h"
        elif char == "c":
            outputString += "e"
        elif char == "d":
            outputString += "s"
        elif char == "e":
            outputString += "o"
        elif char == "f":
            outputString += "c"
        elif char == "g":
            outputString += "v"
        elif char == "h":
            outputString += "x"
        elif char == "i":
            outputString += "d"
        elif char == "j":
            outputString += "u"
        elif char == "k":
            outputString += "i"
        elif char == "l":
            outputString += "g"
        elif char == "m":
            outputString += "l"
        elif char == "n":
            outputString += "b"
        elif char == "o":
            outputString += "k"
        elif char == "p":
            outputString += "r"
        elif char == "q":
            outputString += "z"
        elif char == "r":
            outputString += "t"
        elif char == "s":
            outputString += "n"
        elif char == "t":
            outputString += "w"
        elif char == "u":
            outputString += "j"
        elif char == "v":
            outputString += "p"
        elif char == "w":
            outputString += "f"
        elif char == "x":
            outputString += "m"
        elif char == "y":
            outputString += "a"
        elif char == "z":
            outputString += "q"
        else:
            outputString += char #space case

    print outputString
    outputFile.write("%s"%outputString)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
