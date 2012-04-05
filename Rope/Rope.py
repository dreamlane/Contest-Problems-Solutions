# Rope.py
# Google Code Jam Rope Intranet Round 1C 2010 Problem A
# Benjamin Johnson
# March 12 2012 Large and Small solved in 20 minutes
# Lessons Learned: 

inputFile = open("Rope-large.in","r") #Update these for the problem
outputFile = open("Rope.txt","w") #

testcases = int(inputFile.readline())
for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    print "Case #",str(testcase+1)+": "

    # Solve problem...

    # For every Line where Ai is above Aj, count an intersection when Bi is below Bj
    #    if Ai is below Aj, count an intersection when Bi is above Bj

    #Get the input
    n = int(inputFile.readline())
    lines = []
    for line in range(n):
        lines.append(map(int,inputFile.readline().split()))
    count = 0
    for i in range(n):
        Ai = lines[i][0]
        Bi = lines[i][1]
        for j in range(i,n):
            if i == j:
                continue;
            if Ai > lines[j][0]:
                if Bi < lines[j][1]:
                    count += 1
            else:
                if Bi > lines[j][1]:
                    count += 1

    print count
    outputFile.write("%d"%count)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

