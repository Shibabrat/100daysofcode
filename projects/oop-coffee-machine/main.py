from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turnonCoffeeMachine = True
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
drink_menu = Menu()

while turnonCoffeeMachine:
    action = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if action == "espresso" or action == "latte" or action == "cappuccino":
        drink = drink_menu.find_drink(action)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
    elif action == "report":
        coffee_machine.report()
        money_machine.report()
    elif action == "off":
        print("Turning off the machine")
        turnonCoffeeMachine = False
    else:
        print("Invalid input!")
