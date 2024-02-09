import os
import art
os.system('cls')

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operators = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
        

def calculator():
    os.system('cls')
    print(art.logo)
    cont = "n"
    first_number = float(input("What's the first number?: "))
    for key in operators:
        print(key)

    while cont != 'q':        
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))

        calculated_number = operators[operation](first_number, next_number)

        print(f"{float(first_number)} {operation} {float(next_number)} = {float(calculated_number)}")

        cont = input(f"Type 'y' to continue calculating with {calculated_number}, or type 'n' to start a new calculation: ")

        if cont == "y":
            first_number = calculated_number
        elif cont == "n":
            calculator()
        else:
            quit

calculator()