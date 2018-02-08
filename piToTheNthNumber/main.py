# Print Pi to n places
# Take user input to determine n
# Format number neatly to print in return

from math import pi


def printNPlacesOfPi():
    userInput = input("Enter number of places to print pi to (min = 1, max = 1000):")
    try:
        numberOfPlaces = int(userInput)
    except ValueError:
        print("That's not an integer!")
    if numberOfPlaces > 1000:
        numberOfPlaces = 1000
    if numberOfPlaces < 1:
        numberOfPlaces = 1
    print('{:.{}f}'.format(pi, numberOfPlaces))

printNPlacesOfPi()