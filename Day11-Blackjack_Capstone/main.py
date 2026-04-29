import subprocess
import os
import random
from art import logo

def clean_terminal():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)

def check_11(hand):
    """Check if the hand contains 11, and if it is bigger than 21, so then it remove the 11 and append 1"""
    while sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

def check_result(u_hand: list[int], c_hand: list[int]):
    """Return the result of the program"""
    user_sum = sum(u_hand)
    comp_sum = sum(c_hand)
    len(c_hand)
    len(u_hand)

    # Blackjack?
    if (user_sum == 21 and len(u_hand) == 2) and (comp_sum == 21 and len(c_hand) == 2):
        return "That's a draw!! (Double Blackjack)"
    if user_sum == 21 and len(u_hand) == 2:
        return 'Win with a Blackjack!'
    if comp_sum == 21 and len(c_hand) == 2:
        return 'Lose, computer has a Blackjack!'

    # Checking if the user burst
    if user_sum > 21:
        return 'You went over. You lose...'

    # Checking if the computer burst
    if comp_sum > 21:
        return 'The computer went over. You win!'


    # Comparison between the final points (No one burst)
    if user_sum > comp_sum:
        return 'You win!!'
    elif comp_sum > user_sum:
        return 'You lose...'
    else:
        return "That's a draw!!"


repeat = True
wanna_play = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
if wanna_play == 'n':
    repeat = False

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while repeat:
    clean_terminal()
    print(logo)

    user_hand = [random.choice(cards), random.choice(cards)]
    computer_hand = [random.choice(cards)]

    check_11(user_hand)

    # Continua rodando at� a soma ser menor que 21
    while sum(user_hand) < 21:
        print(f'Your cards: {user_hand}, current score: {sum(user_hand)}')
        print(f"Computer's first card: {computer_hand[0]}")
        decision = input("Type 'y' to get another card, type 'n' to pass: ")

        if decision == 'y':
            user_hand.append(random.choice(cards))
            check_11(user_hand)
        else:
            break

    if sum(user_hand) <= 21:
        while sum(computer_hand) < 17:
            computer_hand.append(random.choice(cards))
            check_11(computer_hand)

    print(f'Your final hand: {user_hand}, final score: {sum(user_hand)}')
    print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")

    print(check_result(u_hand=user_hand, c_hand=computer_hand))

    wanna_play = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
    if wanna_play == 'n':
        repeat = False
