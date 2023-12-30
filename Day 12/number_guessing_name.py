# Imports
import random

# Variables

# Functions
def select_difficulty():
    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        guesses = 10  # 10 guesses
        print("You will have 10 guesses.")
        return guesses
    if difficulty == "hard":
        guesses = 5  # 5 guesses
        print("You will have 5 guesses. Good Luck!")
        return guesses
    else:
        print("Invalid input. Please try again.")
# Main
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
guesses = select_difficulty()
for i in range(guesses):
    print(f"You have {guesses} attempts remaining to guess the number.")
    guess = input("Guess a number: ")
    if int(guess) == number:
        print(f"You got it! The answer was {number}.")
        break
    elif int(guess) > number:
        print("Too high.")
        guesses -= 1
    elif int(guess) < number:
        print("Too low.")
        guesses -= 1