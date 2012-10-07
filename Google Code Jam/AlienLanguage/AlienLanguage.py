# AlienLanguage.py
# Solution to code jam qualification problem Alien Language
# Benjamin Johnson
# March 1 2012 10:52-12:11 (solved small and large)
# Spring Break Problem 1
# Lessons learned: 1. Sometimes it's just better to brute force a problem
#                  2. I need practice in recursion, I believe the recursive
#                     solution to this problem would be much more elegant

inputFile = open("AlienLanguage-large.in","r") #Update these for the problem
outputFile = open("AlienLanguage.txt","w") #

length,words,testcases = map(int,inputFile.readline().split())
# Get the dictionary of words
language = []
for word in range(words):
    language.append(inputFile.readline().strip())

for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)

    # Solve problem
    inputChars = []
    inputWord = (inputFile.readline().strip())
    beginList = False
    charList = []
    for char in inputWord:
        if char == '(':
            charList = []
            beginList = True
            continue
        if char == ')':
            beginList = False
            inputChars.append(charList)
            continue
        if beginList:
            charList.append(char)
        else:
            inputChars.append([char])
    # Now we have a list of lists of chars
    #print inputChars
    # Check how many of the words in the dictionary are possible
    possible = 0
    for word in language:
        for i in range(length):
            if word[i] not in inputChars[i]:
                break
        else:
            possible += 1
    outputFile.write("%d"%possible)        
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

