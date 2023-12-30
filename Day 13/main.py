# Import Random, Logo, and Game Data
from random import randint
from art import logo, vs
from game_data import data

# Variables
score = 0
playing = True

# Functions
def compare(a, b):
    """Compares the follower count between two accounts"""
    if a > b:
        return "a"
    else:
        return "b"

def game():
# Display Welcome and Logo
    print(logo)
    # Randomly Select A and B
    a = data[randint(0, len(data)-1)]
    b = data[randint(0, len(data)-1)]

    # Display A VS B
    print(f"Compare A: {a['name']}, {a['description']} from {a['country']} ")
    print(vs)
    print(f"Compare B: {b['name']}, {b['description']} from {b['country']} ")

    # Ask User for Guess
    guess = input("Who has more followers? Type 'A' or 'B': ")
    # Compare Followers between A and B
    answer = compare(a['follower_count'], b['follower_count'])

    # Check if User is correct or not
    if guess == answer:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print("Sorry, that's wrong. Final Score: 0")
    # Proceed to next question or end game

while playing == True:
    game()