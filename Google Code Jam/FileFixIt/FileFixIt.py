# FileFix-It.py
# Google Code Jam Skeleton for Python
# Benjamin Johnson
# Feb 29 2012: 1:50-2:50,3:09-3:15,4:18-4:24
# Lessons Learned: Even though I understand what a Tree is,
#                   I need to know how to very quickly implement one.
#                  Things that seem simple, become very time consuming
#                   if implementing them for the first time.
#                  The majority of this exercise was spent on building a tree.

# An N-ary tree data structure where the contents of the node are:
#   a title and a list of children nodes
class TreeNode():
    def __init__(self,title):
        self.children = []
        self.title = title

    def __str__(self):
        if self.children != []:
            for child in self.children:
                print child
        else:
            return self.title
    
    def addChild(self,title):
        self.children.append(TreeNode(title))

    def hasChild(self,title):
        has = False
        for child in self.children:
            if child.title == title:
                return True
                break
        return has

    def getChild(self,title):
        for child in self.children:
            if child.title == title:
                return child
                break
        else:
            return None
        

inputFile = open("FileFixIt-large.in","r") #Update these for the problem
outputFile = open("FileFixIt.txt","w") #

testcases = int(inputFile.readline())
for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    print "Case #",str(testcase+1)+": "
    # Solve problem...
    n,m = map(int,inputFile.readline().split())
    root = TreeNode('root') # init the tree with an empty title
    commands_to_build = 0
    # Build a dictionary, that represents the tree,
    #  where the key is the node's path, and the value is the paths of children
    for i in range(n+m):
        path_to_build = inputFile.readline().strip().split('/')
        del path_to_build[0] # get rid of the root node reference
        # traverse the tree until you can go no further
        # Start at the root
        current_node = root
        for directory in path_to_build:
            if current_node.hasChild(directory):
                # move on down the tree
                current_node = current_node.getChild(directory)
            else:
                # add the node
                current_node.addChild(directory)
                current_node = current_node.getChild(directory)
                if i >=n:
                    commands_to_build += 1
    print commands_to_build
    outputFile.write("%d"%commands_to_build)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

