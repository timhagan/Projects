from math import pi


def printNPlacesOfPi():
    while True:
        try:
            # accepts input as integer
            user_input = int(raw_input("Enter number of places to print pi to (min = 1, max = 1000): "))
        except ValueError:
            print("That's not an integer!")
            continue
        if user_input < 0:
            print("Try a positive number!")
        else:
            break

    if user_input > 1000:
            user_input = 1000
    if user_input < 1:
            user_input = 1
    print('{:.{}f}'.format(pi, user_input))

printNPlacesOfPi()

