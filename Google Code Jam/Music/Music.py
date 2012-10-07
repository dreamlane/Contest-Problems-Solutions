# Music.py
# Google Code Jam EuroPython Problem B
# Benjamin Johnson
# March 13 2012
# Lessons Learned: 
#

import sys,math

filename = "Music"

#inputFilename = filename+"-test.in"
#inputFilename = filename+"-small.in"
inputFilename = filename+"-large.in"

outputFilename = filename+".txt"

inputFile = open(inputFilename,"r") 
outputFile = open(outputFilename,"w")

testcases = int(inputFile.readline())
for testcase in range(testcases):
    outputStringHeader = "Case #"+str(testcase+1)+": "
    outputFile.write(outputStringHeader)
    print "Case #",str(testcase+1)+": "

    # Solve problem...
    n = int(inputFile.readline())
    songs = []
    for i in range(n):
        songs.append(inputFile.readline().strip().lower())

    # Find the shortest substring that returns just the 1 song for each song
    for song in songs:
        # Get all of the n-grams for n in range(1,len(song)), until a
        #   unique search is found
        nGram = 0
        found = False
        searches = []
        while not found and nGram <= len(song):
            # Grab all of the nGrams and test them as searches
            for i in range(len(song)+1-nGram):
                search = song[i:i+nGram]
                #print search
                #test the search for only 1 result, if so, valid result found
                # set the loop to break, but continue searching for better searches
                songsFound = 0
                for j in range(len(songs)):
                    if search in songs[j]:
                        songsFound+=1
                if songsFound == 1:
                    found = True
                    searches.append(search.upper())
            nGram += 1

        #sort the searches lexicographicly
        if len(searches) > 0:
            searches.sort()
            outputString = '\n'+'"'+searches[0]+'"'
        else:
            outputString = '\n'+':('
        outputFile.write(outputString)
        #report the best one
        
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

