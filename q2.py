"""
the function will:
    create an array of 0s (each slot denoting the range of 0-10, 11-20, etc)
    opening a file to read given by the parameter
    there is a single number in each line
    for each number, using some weird formmula I made to convert the number into an appropriate index that would increment a value at that index
    close the file
    set up the graph by plotting the points using the array and labeling
    show case the graph
"""
def graphSnowfall(t):
    bars = [0,0,0,0,0]  # data structure to hold the values (for this test case, the numbers are from 0 to 50)
    f = open(t, "r") #open file
    for line in f.readlines(): # reading line by line
        value = int(line) - 1 # to make the next line easier to read, grabbing the value and rounding it down
        bars[int((value)/10)]+= 1
        # by shifting the number down by one and rounding down, the numbers can work themselves
        # into an index value to increment the appropriate slot in the array
    f.close() #close file
    
    x = np.array(["0-10cm", "11-20cm", "21-30cm", "31-40cm", "41-50cm"]) #X-axis label
    y = np.array(bars) # the y value 
    plt.bar(x,y) #plotting the bars
    plt.show() #showing the bar grapgh


graphSnowfall("test.txt")
