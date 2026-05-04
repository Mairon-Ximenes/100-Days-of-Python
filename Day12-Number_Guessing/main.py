import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# welcome e etc
def logo_start():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")


def difficulty_chosen() -> int:
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            return EASY_LEVEL_TURNS
        elif difficulty == "hard":
            return HARD_LEVEL_TURNS
        print("Invalid choice. Please type 'easy' or 'hard'.")


def set_random_number():
    return random.randint(1, 100)


def play_game(attempts: int, random_num: int):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        # is equal
        if guess == random_num:
            print(f"You got it! The answer was {random_num}.")
            break
        elif guess < random_num:
            print("Too low.")

        else:
            print("Too high.")
        attempts -= 1
        if attempts > 0: print("Guess again.")
        else: print(f'You lose! The number was {random_num}')



def main():
    logo_start()
    random_number = set_random_number()
    attempts = difficulty_chosen()
    play_game(attempts, random_number)
    

main()
