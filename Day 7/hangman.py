import random
import hangman_art
import hangman_words
import os

stages = hangman_art.stages

word_list = hangman_words.word_list

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

lives = 6

end_of_game = False

display = []
alfabet = []
letters_used = []

os.system('cls')

print(hangman_art.logo)

for _ in range(len(hangman_words.alfabet)):
    alfabet += "_"

for _ in range(word_length):
    display += "_"

print(F"{' '.join(display)}")

while not end_of_game:
    choice = input("Guess a letter: ").lower()
    os.system('cls')
    if choice in letters_used:
        print(f"Stupid is who stupid does! You've already used letter: {choice}")
        print(F"{' '.join(display)}")
        print(stages[lives])        
    else:
        letters_used.append(choice)

        for i in range(len(alfabet)):
            if hangman_words.alfabet[i] == choice:
                alfabet[i] = choice
        for i in range(word_length):
            if chosen_word[i] == choice:
                display[i] = choice
            
        if choice not in chosen_word:
            lives -= 1
            print(f"Letter {choice} is not in the word. You lose a life. Lives remaining {lives}.")
            if lives == 0:
                end_of_game = True
                print(f"You lose, the word was {chosen_word}")
        else:
            print(f"Letter {choice} is in the word! :D")
        if "_" not in display:
            end_of_game = True
            print("You win")

        print(F"{' '.join(display)}")
        print(stages[lives])
        print("Used words:")
        print(F"{' '.join(alfabet)}")