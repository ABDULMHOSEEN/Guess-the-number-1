# Guess the number game

from random import randint # imports the random integer function from the random module

unknownNumber = randint(1, 10) # sets the range of the unknown number to be generated in

userChoice = int(input("Guess the number from 1 to 10: ")) # prompts the user for the first guess

while userChoice > 10 or userChoice < 0: # validates that the user inputs a number within the specified range
 print("Input outside range. Please try again.") # prints the appropriate message
 userChoice = int(input("Guess the number from 1 to 10: ")) # will keep prompting the user for a correct input if input is out of range

tries = 2 # sets the tries counter to 2
while userChoice != unknownNumber and tries != 0: # checks if the user's input matches the unknown number

    if userChoice > 10 or userChoice < 0 : # validates that the user inputs a number within the specified range
        print("Input outside range. Please try again.")  # prints the appropriate message
        userChoice = int(input("Guess the number from 1 to 10: "))  # will keep prompting the user for a correct input if input is out of range
    else:
        tries = tries - 1  ## the tries counter will be changed accordingly
        print(" Try Again. %d tries remaining " % tries) # if it doesnt match, this message will be printed
        userChoice = int(input("Guess the number from 1 to 10: ")) ## and the user will be prompted again for an input


if userChoice == unknownNumber: # if the user's input matches the unknown number
    print("yay you guessed correctly") ## the following message will be printed
else:
    print('You didnt guess the number in 3 tries. The number was %d' % unknownNumber) # if the user failed to guess, this message will be printed
