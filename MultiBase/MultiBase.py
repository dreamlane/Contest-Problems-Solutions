# MultiBase.py
# Google Code Jam Round 1A 2009
# Benjamin Johnson
# April 24 2012 1:47-
# Lessons Learned: You cant make a list of empty dictionaries using [{}]*9...
#                   ... That will make 9 references to the same dictionary.

import sys,math,time

happyNumbers = [{},{},{},{},{},{},{},{},{}] # [{number: T or F}] where index+2 = base
def digit_to_char(digit):
    if digit < 10: return chr(ord('0') + digit)
    else: return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number,base)
    else:
        (d,m) = divmod(number,base)
        if d:
            return str_base(d,base) + digit_to_char(m)
        else:
            return digit_to_char(m)

def happy(number,base,totals):
    # A number is happy if when taking the squares of its digits sums up to 1

    # First, check to see if the number has been solved in the current base
    if number in happyNumbers[base-2]:
        return happyNumbers[base-2][number]
    # Let's see if the number is happy in its current state
    sumtotal = 0
    ##print "testing:",number,"base:",base,"totals:",totals
    for digit in number:
        sumtotal+=int(digit)
    ##print "sumtotal:",sumtotal
    if sumtotal == 1:
        ##print number,"is happy"
        happyNumbers[base-2][number] = True
        return True
    # Process the next step
    total = 0
    for digit in number:
        total += int(digit)**2
    new_number = str_base(total,base)
    # Let's see if the number has cycled
    if total in totals:
        ##print "number:",total,"has already been tried, cycle reached"
        happyNumbers[base-2][number] = False
        return False
    totals[total] = None
    happyNumbers[base-2][number] = happy(new_number,base,totals)
    return happyNumbers[base-2][number]
    #return happy(new_number,base,totals)
    
filename = "MultiBase"

#inputFilename = filename+"-test.in"
#inputFilename = filename+"-small.in"
inputFilename = filename+"-large.in"

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
    bases = map(int,inputFile.readline().split())
    ##print "bases:",bases
    # Figure out the lowest happy number where all bases are considered, that's our upper bound
    number = 2
    
    while True:
        ##print "checking:",number
        #check to see if the number is happy in all bases
        for base in bases:
            #convert the number to base
            new_number = str_base(number,base)
            ##print number,new_number
            #see if it's happy, if not move to the next number
            if not happy(new_number,base,{}):
                ##print number,"is not happy in base:",base,new_number
                if number%100000 == 0:
                    print number
                break
        else:
            ##print "Happy number found"
            print number
            break            
        number+=1
            
    #print happyNumbers
    outputFile.write("%d"%number)
    # Output a new line for the next problem
    outputFile.write("\n")

outputFile.close()
inputFile.close()

print time.time()-startTime


