menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

coins = {
    "penny": 0.01,
    "dime": 0.10,
    "nickel": 0.05,
    "quarter": 0.25
}

isRunning = True
machine_balance = float(0)


def userInput():
    """Asks for user input to later use in deciding which coffee drink to serve"""
    user_choice = str(input("What would you like? (espresso/latte/cappuccino): "))
    return user_choice


def report():
    """Function for printing out a report for current machine supplies and profit"""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${machine_balance}')


def checkResources(user_input):
    """Check whether machine has enough resources to provide selected drink"""
    outcome = True
    if resources["water"] - menu[user_input]["ingredients"]["water"] < 0:
        print("Sorry there is not enough water.")
        outcome = False

    if len(menu[user_input]["ingredients"]) == 3:
        if resources["milk"] - menu[user_input]["ingredients"]["milk"] < 0:
            print("Sorry there is not enough milk.")
            outcome = False

    if resources["coffee"] - menu[user_input]["ingredients"]["coffee"] < 0:
        print("Sorry there is not enough coffee.")
        outcome = False

    return outcome


def subtractIngredients(user_input):
    """Subtracts selected drink's resources from currently available"""
    if len(menu[user_input]["ingredients"]) == 3:
        resources["water"] -= menu[user_input]["ingredients"]["water"]
        resources["milk"] -= menu[user_input]["ingredients"]["milk"]
        resources["coffee"] -= menu[user_input]["ingredients"]["coffee"]
    else:
        resources["water"] -= menu[user_input]["ingredients"]["water"]
        resources["coffee"] -= menu[user_input]["ingredients"]["coffee"]


def coinsAdded():
    """Asks user to insert desired coin amount.
       Multiplies added coins number with their appropriate values.
       """
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    total_money = coins["penny"]*pennies + coins["dime"]*dimes + coins["nickel"]*nickles + coins["quarter"]*quarters
    print(f"${total_money}")
    return total_money


while isRunning:
    user_choice = userInput()
    if user_choice == "off":
        isRunning = False
    elif user_choice == "report":
        report()

    if user_choice == "latte" or user_choice == "cappuccino" or user_choice == "espresso":
        if checkResources(user_choice):
            total_money = coinsAdded()
            if total_money < menu[user_choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                machine_balance += menu[user_choice]["cost"]
                if total_money > menu[user_choice]["cost"]:
                    change = total_money - menu[user_choice]["cost"]
                    print(f"Here is ${change} dollars in change.")
                total_money -= menu[user_choice]["cost"]
                subtractIngredients(user_choice)
                print(f"Here is your {user_choice}. Enjoy!")
