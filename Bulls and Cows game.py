# importing the necessary libraries
import random
from random import randrange, randint, sample


def Main_game():
    # Generate a random four-digit number for the user to guess
    secret_number = randint(1000, 9999)

    # Convert the number to a string for easier processing
    secret_number_str = str(secret_number)

    # Initialize variables to track the number of bulls and cows
    bulls = 0
    cows = 0

    # Keep track of the number of turns
    counter = 4

    # Main game loop
    while bulls < counter:
        # Prompt the user for a guess
        guess = input("Please enter your 4 digit guess: ")

        # Increment the number of turns
        counter -= 1

        # Convert the guess to a string for easier processing
        guess_str = str(guess)

        # check in if input is valid
        if len(guess_str) < 4 or len(guess_str) > 4:
            print("Type 4 digit number please: \n ")
            return Main_game()

        # Check each digit in the guess and compare it to the secret number
        for i in range(4):
            # Check if the digit is in the correct position
            if guess_str[i] == secret_number_str[i]:
                bulls += 1
            # Check if the digit is in the secret number but in the wrong position
            elif guess_str[i] in secret_number_str:
                cows += 1
        # checking if the user have won the game or else
        if bulls == 4:
            print("You have won the game Congrats: ")
            print("Press 0 to Exit or Any for play it again: ")
            args = int(input(".....: "))
            if args == 0:
                exit()
            else:
                Main_game()

        # Print the number of bulls and cows for this turn
        print(f"Bulls: {bulls}, Cows: {cows}")

        # Reset the number of bulls and cows for the next turn
        bulls = 0
        cows = 0

    # Print a message indicating that the user has guessed the secret number
    print("Your have not succeeded this time please try again")


Main_game()
