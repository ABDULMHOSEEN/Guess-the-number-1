# Guess the number game
# import
from random import randint  # imports the random integer function from the random module
from math import *

# Take value
unknownNumber = randint(1, 100)  # sets the range of the unknown number to be generated in
userChoice = int(input("Guess the number from 1 to 100: "))  # prompts the user for the first guess

# define a function that will say if the guess is far or close
def hot_cold(userChoice):

    distance = abs(unknownNumber - userChoice)
    if distance <= 10:
        print("Hint!")
        print("-" * 38)
        print("the number is too close (range of 10)")
        print("-" * 38)
    elif distance <= 20:
        print("Hint!")
        print("-" * 33)
        print("You are not so far (range of 20)")
        print("-" * 33)
    elif distance <= 30:
        print("Hint!")
        print("-" * 19)
        print("Cold (range of 30)")
        print("-" * 19)
    else:
        pass
    print()
tries = 4   # sets the tries counter to 4
while userChoice != unknownNumber and tries != 0:    # checks if the user's input matches the unknown number

    if userChoice > 100 or userChoice < 1:   # validates that the user inputs a number within the specified range
        print("Input outside range. Please try again.")  # prints the appropriate message
        userChoice = int(input("Guess the number from 1 to 100: "))      # will keep prompting the user for a correct input if input is out of range
    else:
        hot_cold(userChoice)
        tries -= 1    # the tries counter will be changed accordingly
        print(" Try Again. %d tries remaining " % (int(tries) + 1))    # if it doesnt match, this message will be printed
        userChoice = int(input("Guess the number from 1 to 100: "))  # and the user will be prompted again for an input


if userChoice == unknownNumber:     # if the user's input matches the unknown number
    print("\nYah! you guessed correctly")  # the following message will be printed
else:
    print('''You didn't guess the number in 5 tries. The number was %d''' % unknownNumber)   # if the user failed to guess, this message will be printed
