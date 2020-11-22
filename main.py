from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create Menu Item Objects
cappuccino = MenuItem(
    name="cappuccino",
    water=250,
    milk=100,
    coffee=24,
    cost=3.0
)

espresso = MenuItem(
    name="espresso",
    water=50,
    milk=0,
    coffee=18,
    cost=1.5
)

latte = MenuItem(
    name="latte",
    water=200,
    milk=150,
    coffee=24,
    cost=2.5
)

# Create Objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# Get User Drink Selection
def user_selection():
    """Get the user selection.
    Returns: string selection"""
    return input(f"What would you like? ({menu.get_items()}): ").lower()


def machine():

    run_machine = True
    while run_machine:
        choice = user_selection()
        if choice == "off":
            run_machine = False
        elif choice == "report":
            print("Resources:")
            coffee_maker.report()
            print("Profit:")
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink is not None:
                sufficient = coffee_maker.is_resource_sufficient(drink)
                if sufficient:
                    paid = money_machine.make_payment(drink.cost)
                    if paid:
                        coffee_maker.make_coffee(drink)


machine()
