import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.')
choice = int(input())

if choice >= 3 or choice <= 0:
    print('Invalid values')
else:
    print(options[choice])

    computer_choice = random.randint(0, 2)
    print('Computer chose: ')
    print(options[computer_choice])

    if (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
        print('You lose')
    elif choice == computer_choice:
        print("It's a draw")
    else:
        print('You win')
