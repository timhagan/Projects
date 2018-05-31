from math import sqrt
import numpy as np

def printFibSeqToNthNum():
    userInput = input("Enter number of places to print FibSeq to (min = 1, max = 1000):")
    try:
        numberOfPlaces = int(userInput)
    except ValueError:
        print("That's not an integer!")
    if numberOfPlaces > 1000:
        numberOfPlaces = 1000
    if numberOfPlaces < 1:
        numberOfPlaces = 1
    n = np.array([range(0,numberOfPlaces)])
    fibArray = np.array((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
    print(fibArray)

printFibSeqToNthNum()