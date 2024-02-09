import os
import art
os.system('cls')

def calculator(x, y, operator):
    if operator == "+":
        return x+y
    elif operator == "-":
        return x-y
    elif operator == "*":
        return x*y
    elif operator == "/":
        return x/y
        
cont = "n"

while cont != 'q':
    if cont == "n":
        os.system('cls')
        print(art.logo)
        first_number = float(input("What's the first number?: "))
        print("+")
        print("-")
        print("*")
        print("/")
        
    operation = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))

    calculated_number = calculator(first_number, next_number, operation)

    print(f"{float(first_number)} {operation} {float(next_number)} = {float(calculated_number)}")

    cont = input(f"Type 'y' to continue calculating with {calculated_number}, or type 'n' to start a new calculation: ")

    if cont == "y":
        first_number = calculated_number
