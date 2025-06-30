from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_menu = Menu()
my_coffeemaker = CoffeeMaker()
my_money_machine = MoneyMachine()
on = True
while on:
    order = input(f"What would you like? {my_menu.get_items()}")
    drink = my_menu.find_drink(order)
    if order == "report":
        my_coffeemaker.report()
        my_money_machine.report()
    elif order == "off":
        on = False
    else:
        if my_coffeemaker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                 my_coffeemaker.make_coffee(drink)






