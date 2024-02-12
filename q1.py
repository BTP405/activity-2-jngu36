"""
the function will:
    recieve a number as the maximum number to calculate to from 2
    create an empty array
    go into a for loop with range from 2 to n + 1 with count being the numerator
    set a flag to true to determine if its divisible
    do another for loop to run through numbers as the denominator against the numerator
    if count can be divided, make good = false so it does not append to the array
    if good is still true, append the number to the array
    return the array
""""
def getPrimeNumbers(n):
    primeList = [] #create an empty array
    for count in range(2,n+1): #iterate fromm 2 to n+1
        good = True; #set a check 
        for div in range(2,count):
            if (count % div) == 0:
                #with how we set up our for loops, if the number can be divided by modulus, 
                # set the check flag to false so it does not get included to the array
                good = False
                break
        if(good):
            primeList.append(count)
    return primeList
