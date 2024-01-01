# Import Random, Logo, and Game Data
import random
from art import logo, vs
from game_data import data
import os
# Variables
score = 0
playing = True
account_b = random.choice(data)
# Functions
def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a, b):
    """Checks followers against user's guess"""
    if a > b:
        return guess == "a"
    else:
        return guess == "b"

while playing == True:
    # Randomly Select A and B
    account_a = account_b
    account_b = random.choice(data)
    # Remove possibly for duplicates
    if account_a == account_b:
        account_b = random.choice(data)

    # Display A VS B
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask User for Guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Compare Followers between A and B
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system("clear")
    print(logo)
 
    # Check if User is correct or not
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        playing = False
        print(f"Sorry, that's wrong. Final score: {score}")
