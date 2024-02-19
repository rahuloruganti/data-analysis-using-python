#coffee maker using oops concept
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
m=Menu()
cm=CoffeeMaker()
mm=MoneyMachine()
on=True
while on:
    drink=input(f'what would ou like to have? {m.get_items()}')
    if drink=="off":
        on=False
    elif drink=="report":
        print(cm.report())
        print(mm.report())
    else:
        choice=m.find_drink(drink)
        if mm.make_payment(choice.cost):
            if cm.is_resource_sufficient(choice):
                cm.make_coffee(choice)