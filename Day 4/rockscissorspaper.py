import random

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if human_choice not in (0,1,2):
    print("Stupid is who stupid does. You lose!")
    exit()
computer_choice = random.randint(0,2)

choices = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
print(choices[human_choice])

print("Computer chose:")

print(choices[computer_choice])

if human_choice == computer_choice:
    print("It's a draw")
elif (human_choice == 0 and computer_choice == 2) or (human_choice == 1 and computer_choice == 0) or (human_choice == 2 and computer_choice == 1):
    print("You won!")
else:
    print("You lose")
