# Building.py
# Google Code Jam 2011 Africa Qual
# Benjamin Johnson
# March 14 2012 9:00-9:33 Stumped
# Lessons Learned: 

import sys,math,random,time

filename = "Building"

#inputFilename = filename+"-test.in"
#inputFilename = filename+"-small.in"
inputFilename = filename+"-large.in"

outputFilename = filename+".txt"

inputFile = open(inputFilename,"r") #Update these for the problem
outputFile = open(outputFilename,"w") #

testcases = int(inputFile.readline())
starttime = time.time()
for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    #print "Case #",str(testcase+1)+": "

    # Solve problem...
    length,width = map(int,inputFile.readline().split())
    plot = []
    for i in range(width):
        plot.append(inputFile.readline().strip())

    newPlot = []
    for row in plot:
        newRow = []
        for i in range(length):
            if row[i] in "TWR":
                newRow.append(0)
            else:
                newRow.append(1)
        newPlot.append(newRow)
        plot = newPlot

    indices = []
    for i in range(len(plot)):
        for j in range(len(plot[i])):
            indices.append((i,j))
    #print indices
    #random.shuffle(indices)
    
    # Now the problem is the same as the dynamic programming submatrix problem
    #    from the 2010 ACM competition... Actually it's not, it wants the largest rectangle
    #    not the largest square
    biggest = 0
    #print width,length
    #Brute Force

    for index in indices:
        cW = len(plot[index[0]])-index[1]
        cH = len(plot)-index[0]

        if cW*cH > biggest:
            while cW != 0 and cH != 0:
                while cH != 0:
                    if cW*cH > biggest:
                        for i in range(cH):
                            zeroFound = False
                            for j in range(cW):
                                #print index
                                #print i+index[0],j+index[1]
                                if plot[i+index[0]][j+index[1]] == 0:
                                    zeroFound = True
                                    break
                            if zeroFound:
                                break
                        else:
                            #print "all 1's found where i = "+str(index)
                            #print "width = "+str(cW)
                            #print "height = "+str(cH)
                            if cW*cH > biggest:
                                biggest = cW*cH
                    cH -= 1
                cH = len(plot)-index[0]
                cW -= 1
        
    
    print biggest
    outputFile.write("%d"%biggest)
    # Output a new line for the next problem
    outputFile.write("\n")


outputFile.close()
inputFile.close()
print time.time()-starttime
