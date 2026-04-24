import os
from art import logo

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bids):
    winner = ''
    bigger = None
    for key in bids:
        if bigger is None or bids[key] > bigger:
            bigger = bids[key]
            winner = key
    clear_terminal()
    print(f'The winner is {winner} with a bid of ${bids[winner]}')

print(logo)
print('Welcome to the secret auction program.')
repeat = True

users_bids = {}

while repeat:
    name = input('What is the name?: ')
    price = int(input('What\'s your bid?: $'))
    users_bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear_terminal()
    while other_bidders != 'no' and other_bidders != 'yes':
        print('Invalid answer. Please try again.')
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        clear_terminal()

    if other_bidders == 'no': repeat = False

find_highest_bidder(users_bids)
