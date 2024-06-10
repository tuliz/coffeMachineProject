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

#varaibles initialization
money = 0
power = True

#return the resources in print format
def printReport(resources):
    """return the report of resources in printable format."""
    return f'Water: {resources["water"]}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}\n'

#sending the answer the customer chosen (if its latte/cappuchino/espresso) and checking if resources are sufficient for making this drink
def checkResources(drinkType, resources):
    """getting the drinkType from Menu the customer chosen and returning True or False if resources sufficient."""

    #looping trough MENU and finding the dring that was chosen
    for drink in MENU:
        if drink == drinkType:
            if resources["water"] >= MENU[drink]['ingredients']['water'] and resources["milk"] >= MENU[drink]['ingredients']['milk'] and resources["coffee"] >= MENU[drink]['ingredients']['coffee']:
                return True
            if resources["water"] < MENU[drink]['ingredients']['water']:
                print('Not enough water]\n')
                return False
            if resources["milk"] < MENU[drink]['ingredients']['milk']:
                print('Not enough milk]\n')
                return False
            if resources["milk"] < MENU[drink]['ingredients']['coffee']:
                print('Not enough coffee]\n')
                return False

#when there are enough resources for the drinks, getting the drinkType and resources and deducting the used resources for the drink           
def useResources(drinktype, resources):
    """getting the drink type and resources if sufficient resources and returning resources after deducting the used recources for the drink."""
    for resource in resources:
        resources[resource] -= MENU[drinktype]["ingredients"][resource]
    return resources


#coffe machine start
def coffeMachine():
    
    resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
    
    while power:
        answer = input("What would you like? (espresso/latte/cappuccino):").lower()
        if answer == 'off':
            return
        elif answer == 'report':
            print(printReport(resources))
        elif answer == 'espresso' or answer == 'latte' or answer == 'cappuccino':
            if not checkResources(drinkType=answer, resources=resources):
                continue
            else:
                resources = useResources(drinktype=answer, resources=resources)


coffeMachine()
