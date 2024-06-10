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

#varaibles initialization
money = 0
power = True

#return the resources in print format
def printReport():
    """return the report of resources in printable format."""
    return f'Water: {resources["water"]}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}\n'

#coffe machine start
def coffeMachine():
    while power:
        answer = input("What would you like? (espresso/latte/cappuccino):")
        if answer == 'off':
            return
        elif answer == 'report':
            print(printReport())



coffeMachine()
