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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resourse_sufficient(order_ingredients):
    """Return the True when order can be mode and False if there is not enough item"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough=False
    return is_enough

def is_transtion_successful(money_recived, drink_cost):
    if money_recived>=drink_cost:
        change=round(money_recived-drink_cost, 2)
        print(f"Here is ${change} change ")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry thats not enough money")
        return False

def process_coins():
    """Return the total calculation from the coin"""
    print("please insert  coin")
    total=int(input("How many of quaters")) * 0.25
    total += int(input("How many of dimes")) * 0.1
    total += int(input("How many of nikles")) * 0.05
    total += int(input("How many of pennies")) * 0.01
    return total

def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here is your {drink_name} ☕️")
is_on=True
while True:
    Choice=input("What would you like? espresso/latte/cappuccino ")
    if Choice=="off":
        is_on=False
    elif Choice=="report":
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        print(f"Water: {resources['water']}ml")
    else:
        drink=MENU[Choice]
        if is_resourse_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transtion_successful(payment, drink["cost"]):
                make_coffe(Choice, drink["ingredients"])





