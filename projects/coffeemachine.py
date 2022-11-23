MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_coffee(drink, resources, menu):
    """ Update the resources after making the last drink"""

    insufficientResources = False
    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        if resources["water"] < menu[drink]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            insufficientResources = True
        elif drink != "espresso" and resources["milk"] < menu[drink]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            insufficientResources = True
        elif resources["coffee"] < menu[drink]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            insufficientResources = True
        else:
            resources["water"] -= menu[drink]["ingredients"]["water"]
            if drink != "espresso":
                resources["milk"] -= menu[drink]["ingredients"]["milk"]
            resources["coffee"] -= menu[drink]["ingredients"]["coffee"]
    else:
        print("Invalid drink")

    return resources, insufficientResources


def print_resources(resources):

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

    return None


def process_coins(drink, menu):

    print(f"{drink} costs: {menu[drink]['cost']}")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    moneyReceived = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if moneyReceived < menu[drink]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        purchaseSuccess = False
    elif moneyReceived >= menu[drink]["cost"]:
        print(f"Here is ${round(moneyReceived - menu[drink]['cost'], 2)} in change.")
        resources["money"] += menu[drink]["cost"]
        purchaseSuccess = True

    return purchaseSuccess


turnonCoffeeMachine = True
resources["money"] = 0
while turnonCoffeeMachine:
    action = input("What would you like? (espresso/latte/cappuccino): ")
    if action == "espresso" or action == "latte" or action == "cappuccino":
        if resources["water"] != 0 and resources["milk"] != 0 and resources["coffee"] != 0:
            print("Please insert coins.")
            if process_coins(action, MENU):
                resources, insufficientResources = make_coffee(action, resources, MENU)
                if not insufficientResources:
                    print(f"Here is your {action} Enjoy!")
    elif action == "report":
        print_resources(resources)
    elif action == "off":
        print("Turning off the machine")
        turnonCoffeeMachine = False
    else:
        print("Invalid input!")
