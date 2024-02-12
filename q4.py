"""
the function: 
    recieves a parameter which contains the name of a file.
    reads the file and line by line
    split the numbers (assuming)
    does a bunch of counting and calcuating
    output the results based on the numbers given per line until the end
"""

def printStats(t):
    f = open(t, "r") # opening file
    linecount = 1
    for line in f.readlines():
        print("line " + str(linecount) + ":")
        #setting up the initial numbers for every iteration
        count = 0
        highest = 0
        average = 0
        linecount += 1 
        for number in line.split(): #reading each line and splitting every number
            num = int(number) # to easier write code
            print (num, end=' ') # print out each number
            count+= 1 # increase the count for every number
            if(int(num) > highest): # checking to see the current number beats the highest
                highest = num
            average += num # adding to a total to divide by count later for the average

        # print everything
        print("\nthe count of the numbers read: " + str(count))
        print("the average of the numbers: " + str(average/count))
        print("the maximum of the numbers: " + str(highest) + "\n")
    f.close() # close file
