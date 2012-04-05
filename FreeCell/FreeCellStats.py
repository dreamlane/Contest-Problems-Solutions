# FreeCellStats.py
# Solution to Numbers problem, Google Code Jam Round 1A 2008 Problem C
# Benjamin Johnson
# Feb 28 2012 3:34-4:09 = 35 minutes + 1 missed attempt
# Lessons learned: Need to learn matrices, and need to determine if numpy is available at acm ICPC

import math

inputFile = open("FreeCell-large.in","r")
outputFile = open("FreeCell.txt","w")
testcases = int(inputFile.readline())
EPS = 0.0001
for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    print "Case #",str(testcase+1)+": "

    # Solve problem...
    games_today, percent_today, percent_total = map(int,inputFile.readline().split())
    possible = False
    if percent_total == 100:
        if percent_today == 100:
            outputFile.write("Possible")
        else:
            outputFile.write("Broken")
    elif percent_total == 0:
        if percent_today == 0:
            outputFile.write("Possible")
        else:
            outputFile.write("Broken")
    else:
        if games_today >= 100:
            outputFile.write("Possible")
        # determine the games won and played today
        else:
            for played in range(1,games_today+1):
                for wins in range(1,played+1):
                    percentage = float(wins)/float(played)*100
                    #print "Max games:",games_today,", possible percentage: ",percentage
                    if abs(percentage-percent_today)<EPS:
                        possible = True
                        outputFile.write("Possible")
                        break
                if possible:
                    break
            else:
                outputFile.write("Broken")
                
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

