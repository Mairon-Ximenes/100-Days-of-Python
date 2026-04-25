import os
from art import logo

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

repeat = True
first_number = None

while repeat:
    if first_number is None:
        print(logo)
        first_number = float(input('What is the first number?: '))

    for operation in operations:
        print(f' {operation}')

    operation_chosen = input('Pick an operation: ')
    actual_function = operations[operation_chosen]
    next_number = float(input('What is the next number?: '))

    if operation_chosen == '/' and next_number == 0:
        print("Error: It is not possible to divide a number by zero, please try again.")
        continue

    result = actual_function(first_number, next_number)
    print(f'{first_number} {operation_chosen} {next_number} = {result}')

    want_continue = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'exit' to exit the calculator: ").lower()

    if want_continue == 'y':
        first_number = result
    elif want_continue == 'n':
        clear_terminal()
        first_number = None
    else:
        repeat = False
        print('Thanks for using Python Calc!')
