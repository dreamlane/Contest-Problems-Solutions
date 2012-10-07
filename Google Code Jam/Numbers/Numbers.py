# Numbers.py
# Solution to Numbers problem, Google Code Jam Round 1A 2008 Problem C
# Benjamin Johnson
# Feb 27 2012
# Lessons learned: Need to learn matrices, and need to determine if numpy is available at acm ICPC

import math

inputFile = open("Numbers-small.in","r")
outputFile = open("Numbers.txt","w")
testcases = int(inputFile.readline())

for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    print "Case #",str(testcase+1)+": "

    # Solve problem... easy for the small case
    exponent = int(inputFile.readline())
    coefficient = 3 + math.sqrt(5)
    number = pow(coefficient,exponent)
    print '{0:f}'.format(number)
    print '{0:f}'.format(exponentiation(coefficient,exponent))
    solution = str(number).split('.')[0]
    solution = int(solution)%1000
    outputFile.write("%03d"%int(solution))
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

