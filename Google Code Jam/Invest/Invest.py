# Invest.py
# Google Code Jam 2011 Africa Qual problem 2
# Benjamin Johnson
# March 14 2012 12:24am-12:57
# Lessons Learned: Every piece of code i write has at least one bug in it initially

import sys,math

filename = "Invest"

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
    M = int(inputFile.readline())
    prices = map(int,inputFile.readline().split())

    profit = 0
    buyI = None
    sellI = None
    for i in range(11):
        purchasable = M/prices[i]
        for j in range(i,12):
            if (prices[j]-prices[i])*purchasable > profit and prices[i] <= M:
                profit = (prices[j]-prices[i])*purchasable
                buyI = i
                sellI = j
            elif (prices[j]-prices[i])*purchasable == profit and prices[i] <= M:
                if buyI and prices[buyI] < prices[i]:
                    profit = (prices[j]-price[i])*purchasable
                else:
                    buyI = i
                    sellI = j

    if profit <= 0:
        outputFile.write("IMPOSSIBLE")
        print "IMPOSSIBLE"
    else:
        outputString = str(buyI+1)+" "+str(sellI+1)+" "+str(profit)
        outputFile.write(outputString)
        print outputString
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()
