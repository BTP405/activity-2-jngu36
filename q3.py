"""
the function will:
    create an empty dictionary
    read the file given in the parameter
    for every line read, split the words up
    for ease, convert all lowercase to uppercase
    if the word doesnt exist in the keyword, create a value of 1 with the word as the keyword
    if it does exist, increment the value by 1
    close the connection and print the dictionary
"""
def wordCount(t):
    t_dict = {} # empty dictionary
    f = open(t, "r") # opening file
    for line in f.readlines(): 
        for word in line.split(): #reading each line and splitting every word
            if word.upper() in t_dict: #if the word exists in the dictionary, increment. otherwise, create the inital value
                t_dict[word.upper()] += 1
            else:
                t_dict[word.upper()] = 1

    f.close() # close file
    print(t_dict) # print
