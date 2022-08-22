# aim of the programming is to create a software for coffee machine
# the code can be refactored to to look shorter and better


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
    },
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def user_order(user_request):
    if user_request == 'report':
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${profit}")

    elif user_request == 'espresso':
        process_order(order='espresso', water=MENU['espresso']['ingredients']['water'], milk=0,
                      coffee=MENU['espresso']['ingredients']['coffee'], price=MENU['espresso']['cost'])
    elif user_request == 'latte':
        process_order(order='latte', water=MENU['latte']['ingredients']['water'],
                      milk=MENU['latte']['ingredients']['milk'],
                      coffee=MENU['latte']['ingredients']['coffee'], price=MENU['latte']['cost'])
    elif user_request == 'cappuccino':
        process_order(order='cappuccino', water=MENU['cappuccino']['ingredients']['water'],
                      milk=MENU['cappuccino']['ingredients']['milk'],
                      coffee=MENU['cappuccino']['ingredients']['coffee'], price=MENU['cappuccino']['cost'])


def process_order(order, water, milk, coffee, price):
    global profit
    print("Please insert coins.")
    quarters_inserted = float(input("How many Quarters ?: ")) * 0.25
    dimes_inserted = float(input("How many Dimes ?: ")) * 0.10
    nickles_inserted = float(input("How many Nickles ?: ")) * 0.05
    pennies_inserted = float(input("How many Pennies ?: ")) * 0.01

    total = pennies_inserted + nickles_inserted + dimes_inserted + quarters_inserted

    if total < MENU[order]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if coffee < resources['coffee'] and water < resources['water'] and milk < resources['milk']:
            if order == 'espresso':
                resources['water'] = resources['water'] - water
                resources['coffee'] = resources['coffee'] - coffee
                profit += price
                print(f"Here is ${total - price} in change.\n Here is your espresso ☕ Enjoy! ")
            elif order == 'latte':
                resources['water'] = resources['water'] - water
                resources['coffee'] = resources['coffee'] - coffee
                resources['milk'] = resources['milk'] - milk
                profit += price
                print(f"Here is ${total - price} in change.\n Here is your latte ☕ Enjoy! ")
            elif order == 'cappuccino':
                resources['water'] = resources['water'] - water
                resources['coffee'] = resources['coffee'] - coffee
                resources['milk'] = resources['milk'] - milk
                profit += price
                print(f"Here is ${total - price} in change.\n Here is your latte ☕ Enjoy! ")

        elif water > resources['water']:
            print("Sorry there is not enough water.")
        elif coffee > resources['coffee']:
            print("Sorry there is not enough coffee.")
        elif milk > resources['milk']:
            print("Sorry there is not enough milk.")

power = True

while power:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == 'off':
        power = False

    user_order(user_input)
