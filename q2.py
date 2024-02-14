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
import matplotlib.pyplot as plt
import numpy as np

def graphSnowfall(t):
    bars = {}  # data structure to hold the values (for this test case, the numbers are from 0 to 50)
    f = open(t, "r") #open file
    for line in f.readlines(): # reading line by line
        value = int((int(line) - 1)/10) # to make the next line easier to read, grabbing the value and rounding it down
        if value in bars:
            bars[value] +=1
        else:
            bars[value] = 1
        # by shifting the number down by one and rounding down, the numbers can work themselves
        # into an index value to increment the appropriate slot in the array
    f.close() #close file

    # a whole ton of converting

    #generating x labels
    x_label = []
    for keys in bars:
        if(keys == 0):
            x_label.append("0-10")
        else:
            x_label.append(str((keys * 10)+1) + " - " + str((keys+1) * 10))
            
    # since bars is a dictionary and plot needs an array, generate an array
    # each value corresponds to each label
            
    y_values = []
    for y in bars:
        y_values.append(bars[y])

    # plot the things
    x = np.array(x_label) #X-axis label
    y = np.array(y_values) # the y value 
    plt.bar(x,y) #plotting the bars
    plt.show() #showing the bar graph
