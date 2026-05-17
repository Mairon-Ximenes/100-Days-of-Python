import data
import os
import art

# YOU CAN TYPE 'OFF' TO TURN OFF THE COFFEE MACHINE
# OR TYPE 'REPORT' TO SHOWS YOU THE REPORT OF THE MACHINE

# TODO 1: Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
MENU = data.MENU

def clean_terminal():
    """Clean the terminal"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def welcome():
    """Shows the coffee machine logo"""
    print(art.logo)

def print_resources(resources: dict, total_money: float):
    """Print the formatted form of the resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_money:.2f}")

def check_resources(user_choice: str, menu: dict, resources: dict) -> bool:
    """Check if it has sufficient resources in the machine. In case of no, return False"""
    drink: dict = menu[user_choice]
    ingredients:dict = drink["ingredients"]

    for value in ingredients:
        if ingredients[value] > resources[value]:
            print(f"Sorry, there is no enough {value}")
            return False

    return True

def process_coins(drink: dict) -> float:
    """Process the payment with coins, then return the value to add to the total value"""
    value_drink = drink['cost']
    print(f"That drink costs ${value_drink:.2f}")
    print('Please insert coins: ')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))

    total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)


    # TODO 6: Check transaction successful?
    if total < value_drink:
        return 0

    print(f"Total: ${total:.2f}")
    if total > value_drink:
        change = round(total - value_drink, 2)
        print(f"Here is ${change:.2f} in change.")

    return value_drink

def process_resources(drink: dict, resources: dict):
    """Process the resources and update the values"""
    ingredients = drink['ingredients']
    for value in ingredients:
        resources[value] -= ingredients[value]

def main():
    resources = data.resources
    repeat = True
    total_money = 0

    while repeat:
        clean_terminal()
        welcome()
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        print("==========//==========")
        # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
        if user_choice == 'off':
            print('Thank you for using our Coffee Machine!')
            break
        # TODO 3: Print report when the user enters "report"
        elif user_choice == 'report':
            print_resources(resources, total_money)
        else:

            if user_choice in MENU:
                drink: dict = MENU[user_choice]
                # TODO 4: Check resources sufficient?
                if check_resources(user_choice, MENU, resources):
                    # TODO 5: Process coins.
                    coins = process_coins(drink)
                    if coins == 0:
                        print("Sorry that's not enough money. Money refunded.")
                    else:
                        total_money += coins
                        # TODO 7: Make Coffee.
                        process_resources(drink, resources)
                        print(f"Here's your {user_choice}☕! Enjoy.")

            else:
                print('Invalid value. Please try again')

        input('Type enter to continue...')

main()




