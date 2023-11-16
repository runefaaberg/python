print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
  elif age < 18:
    bill = 7
  elif age >= 45 or age <= 55:
    bill = 0
  else:
    bill = 12
  
  want_photo = input("Do you want to buy a ticket? (y/n) ")
  if want_photo == "y":
    bill += 3

  print(f"Your bill is {bill} dollars.")
else:
  print("Sorry, you are too short to ride the rollercoaster.")