import menu

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${profit}")


def enough_resources(water, milk, coffee):
    return water <= resources["water"] and milk <= resources["milk"] and coffee <= resources["coffee"]


def reduce_resources(coffee_type):
    resources["water"] = resources["water"] - menu.MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - menu.MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_type != "espresso":
        resources["milk"] = resources["milk"] - menu.MENU[coffee_type]["ingredients"]["milk"]


def check_resources(coffee_type):
    water = menu.MENU[coffee_type]["ingredients"]["water"]
    coffee = menu.MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_type != "espresso":
        milk = menu.MENU[coffee_type]["ingredients"]["milk"]
    else:
        milk = 0

    # print(f"Water: {water} Milk: {milk} Coffee: {coffee}")
    return enough_resources(water, milk, coffee)


def enough_money(coffee_type, num_penny, num_nickel, num_dime, num_quarter):
    penny_worth = 0.01
    nickel_worth = 0.05
    dime_worth = 0.10
    quarter_worth = 0.25

    total = (penny_worth*num_penny)+(nickel_worth*num_nickel)+(dime_worth*num_dime)+(quarter_worth*num_quarter)

    return total - menu.MENU[coffee_type]["cost"]


def get_missing_resource(coffee_type):
    if resources["water"] < menu.MENU[coffee_type]["ingredients"]["water"]:
        return "water"
    elif resources["coffee"] < menu.MENU[coffee_type]["ingredients"]["coffee"]:
        return "coffee"
    elif resources["milk"] < menu.MENU[coffee_type]["ingredients"]["milk"]:
        return "milk"


choice = ''
while choice != "stop":
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "stop":
        exit()
    elif choice == "report":
        print_report()
    else:
        can_make_coffee = check_resources(choice)

        if can_make_coffee:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            change = enough_money(choice, pennies, nickles, dimes, quarters)
            if change >= 0:
                if change > 0:
                    print(f"Here is ${change} in change.")
                print(f"Here is your {choice}. Enjoy!")
                reduce_resources(choice)
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {get_missing_resource(choice)}")
