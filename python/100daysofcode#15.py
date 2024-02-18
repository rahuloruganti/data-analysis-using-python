#coffee machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def enough_resources(ingredient):
    for i in ingredient:
        if ingredient[i]<resources[i]:
            resources[i]-=ingredient[i]
            return True
        else:
            print(f"insufficent ingredient {i}")
            return False

def cash():
    print("insert coins")
    total=int(input("no.of tens? "))*10
    total+=int(input("no.of five? "))*5
    total+=int(input("no.of two? "))*2
    total+=int(input("no.of one? "))*1
    return total

def valid_transaction(amount,drink_cost):
    if drink_cost<=amount:
         change=amount-drink_cost
         print(f"here is your Rs{change} change")
         return True
    else:
        print("insufficent money. money refunded.")
        return False

on=True
while on:
    coff=input("what would you like to have?(espresso/latte/cappuccino) ")
    if coff=="off":
        on=False
    elif coff=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[coff]
        if enough_resources(drink["ingredients"]):
            pay=cash()
            if valid_transaction(pay,drink["cost"]):
                print(f"here is your {coff} enjoy:)")


                        
            




