from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

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

print(f"cappuccino.ingredients: {cappuccino.ingredients}")
print()

menu = Menu()
print(f"menu.get_items(): {menu.get_items()}")
print()
print(f"menu.find_drink('cappuccino').ingredients: {menu.find_drink('cappuccino').ingredients}")
print()

coffee_maker = CoffeeMaker()
print(f"coffee_maker.report(): {coffee_maker.report()}")  # No return value, hence prints 'None'
print()
print(f"coffee_maker.is_resource_sufficient(cappuccino): {coffee_maker.is_resource_sufficient(cappuccino)}")
print()
print(f"coffee_maker.make_coffee(cappuccino): {coffee_maker.make_coffee(cappuccino)}")  # No return value, hence prints 'None'
print()
print(f"coffee_maker.report(): {coffee_maker.report()}")  # No return value, hence prints 'None'
print()

money_machine = MoneyMachine()
print(f"money_machine.make_payment(menu.find_drink('cappuccino'').cost): {money_machine.make_payment(menu.find_drink('cappuccino').cost)}")
print()
print(f"money_machine.report(): {money_machine.report()}")  # No return value, hence prints 'None'
print()
print(f"coffee_maker.report(): {coffee_maker.report()}")  # No return value, hence prints 'None'
print()