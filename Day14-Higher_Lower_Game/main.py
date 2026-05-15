import os
import art
import game_data
import random

# TODO 1: MAKE A FUNCTION THAT CLEAN THE TERMINAL

def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# TODO 2: MAKE A FUNCTION THAT SHOW THE LOGO

def start():
    clean_terminal()
    print(art.logo)

# TODO 3: IMPORT THE game_data.py data AND SELECT RANDOMLY TWO OF THE ACCOUNTS
def random_accounts() -> list:
    accounts_list = []
    for _ in range(2):
        account = random.choice(game_data.data)
        while account in accounts_list:
            account = random.choice(game_data.data)
        accounts_list.append(account)

    return accounts_list

def change_account(old_account: dict) -> dict:
    account = random.choice(game_data.data)
    while account == old_account:
        account = random.choice(game_data.data)
    return account

# TODO 4: COMPARE THE ACCOUNTS AND CHECK WHICH ONE HAS MORE FOLLOWERS

def check(user_choice:str, a:dict, b:dict, current_score: int) -> int:
    bigger = ''

    if a['follower_count'] > b['follower_count']:
        bigger = 'a'
    else:
        bigger = 'b'

    if user_choice == bigger:
        return current_score + 1
    else:
        return 0


# TODO 5: REPEAT THE PROCESS AND ACCUMULATE THE USER'S SCORE UNTIL HE MISTAKES
def print_option(person:dict) -> str:
    return f"{person['name']}, a {person['description']}, from {person['country']}."


def play(accounts: list):
    repeat = True
    current_score = 0

    account_a: dict = accounts[0]
    account_b: dict = accounts[1]

    # TODO 6: SET THE ACCOUNT A AS ACCOUNT B AND SELECT ANOTHER RANDOM ACCOUNT AND SET IT TO ACCOUNT B
    while repeat:
        start()

        if current_score != 0:
            print(f"You're right! Current score: {current_score}")

        print(f'Compare A: {print_option(account_a)} with {account_a['follower_count']} million followers.')
        print(art.vs)
        print(f'Against B: {print_option(account_b)} with ??? million followers.')
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        round_score = check(user_choice, account_a, account_b, current_score)

        if round_score == 0:
            start()
            print(f"Account A: {account_a['name']} | Followers: {account_a['follower_count']} million")
            print(f"Account B: {account_b['name']} | Followers: {account_b['follower_count']} million")
            print(f"Sorry, that's wrong.")

            print(f"Final score: {current_score}")
            return
        current_score = round_score
        account_a = account_b
        account_b = change_account(old_account=account_a)


def main():
    play(random_accounts())

main()