import random
import os
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def get_attempts(user_level):
    if user_level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def run_game():
    
    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You've got it! The answer was {number}.")
        return True
    elif guess < number:
        print("Too low")
        return False
    else:
        print("Too high")
        return False

def start_game():

    os.system('cls')
    print(art.logo)
    print("Welcome to th Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    game_finished = False

    attempts = get_attempts(level)

    while not game_finished:
        print(f"You have {attempts} remaining to guess the number.")
        game_finished = run_game()
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            game_finished = True
        elif not game_finished:
            print("Guess again.")

number = random.randint(1,100)
start_game()