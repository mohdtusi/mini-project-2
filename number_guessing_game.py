# Simple Number Guessing Game
# Author: Mohammed
# Description:
# A fun Python game where the user has 10 chances to guess a randomly generated number between 1 and 100.


import random

# Greet the player
print("Welcome! Can you find the hidden number??\n")

# Generate a random number between 1 and 100
num = random.randint(1, 100)

# The total number of attempts
attempts = 10

# Loop for each attempt
for i in range(attempts):
    remaining = attempts - i
    print(f"You have {remaining} chance left.")

    try:
        # Ask the player for their guess
        user = int(input("What's your guess?: "))

        # Check if the guess is correct
        if user == num:
            print("You actually did it! Congrats 🎉")
            break
        # Give hints to the player
        elif user < num:
            print("Go Higher ⬆️")
        else:
            print("Go Lower ⬇️")

    # Handle non-numeric input errors
    except ValueError:
        print("Please enter a valid number.")

# If the loop finishes without a correct guess
else:
    print(f"Better luck next time! The number was {num}.")
