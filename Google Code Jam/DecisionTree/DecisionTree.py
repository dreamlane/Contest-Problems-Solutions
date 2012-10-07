# DecisionTree.py
# Google Code Jam 2009 1B A: http://code.google.com/codejam/contest/186264/dashboard
# Benjamin Johnson
# April 25 2012: 8:55-9:48 - Stumped building the tree
# Lessons Learned: Learn more list comprehension and string manipulation

import sys,math,time

filename = "DecisionTree"

inputFilename = filename+"-test.in"
#inputFilename = filename+"-small.in"
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
    # Step one build the tree from the inputs
    # use a dictionary where {key:[p,leftKey,rightKey]}, where leaves left/right = None
    # ... and leaves have key = parentName_l parentName_r
    tree = {}
    num_lines = int(inputFile.readline())
    inputLines = []
    currentParent = None
    for i in xrange(num_lines):
        inputLines.append(inputFile.readline().strip())
    for line in inputLines:
        # If we don't have a parent, then we're working with the root
        if not currentParent:
            # remove the opening paren
            line = line.replace("(","")
            # get the value and feature name
            rootValues = line.split()
            p = rootValues[0]
            trait = rootValues[1]
            tree[trait] = [p,None,None,None]
            # set the current parent to the root, and then work its children
            currentParent = trait
        else: # not the root node
            if line == ")":
                # we've reached the end of a branch, we need to back up to the currentParent's parent
                currentParent = tree[currentParent][3]
                if not currentParent:
                    print "Backing up a level is broken, or"
                continue # Move to the next line
            # We've got a parent, so we need to add this node as a child of the parent
            left = None
            if tree[currentParent][1] == None:
                left = True
            elif tree[currentParent][2] == None:
                left = False
            else:
                #The parent already has 2 children, so the parent should have changed
                print "parent already has 2 children, something is broken"
            
    

    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime
