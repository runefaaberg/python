import random
import os
from art import logo,vs
from game_data import data

contest_A = ''
contest_B = ''

def get_contestant():
    return random.choice(data)

def format_data(contestant):
    return f"{contestant["name"]}, a {contestant["description"]}, from {contestant["country"]}"

def game():
    game_alive = True
    
    score = 0

    contestant_A = get_contestant()
    contestant_B = get_contestant()

    os.system('cls')
    print(logo)

    
    while game_alive:
        while contestant_A == contestant_B:
            contestant_B = get_contestant()

        print(f"Compare A: {format_data(contestant_A)}")
        print(vs)
        print(f"Against B: {format_data(contestant_B)}")

        get_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        os.system('cls')
        print(logo)

        if (get_choice == 'A' and contestant_A["follower_count"] < contestant_B["follower_count"]) or (get_choice == 'B' and contestant_A["follower_count"] > contestant_B["follower_count"]):
            game_alive = False
            print(f"Sorry, that's wrong. Final score: {score}")
        else:
            score += 1
            print(f"You're right! Current score: {score}.")
            contestant_A = contestant_B
            contestant_B = get_contestant()

game()

