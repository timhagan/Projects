from math import e

def printNPlacesOfe():
    userInput = input("Enter number of places to print e to (min = 1, max = 1000):")
    try:
        numberOfPlaces = int(userInput)
    except ValueError:
        print("That's not an integer!")
    if numberOfPlaces > 1000:
        numberOfPlaces = 1000
    if numberOfPlaces < 1:
        numberOfPlaces = 1
    print('{:.{}f}'.format(e, numberOfPlaces))

printNPlacesOfe()