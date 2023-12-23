import os
import art

bidders = {}

new_bidder = True

os.system('cls')

print(art.logo)
while new_bidder:
    name = input("What is your name?:")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
    
    if another_bidder == "no":
        new_bidder = False
    os.system('cls')

high_bid = 0

for bidder in bidders:
    if bidders[bidder] > high_bid:
        Winner = bidder

print(f"The winner is {Winner} with a bid of $ {bidders[Winner]}.")