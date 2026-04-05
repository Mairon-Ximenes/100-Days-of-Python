print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go? ")
direction = input('\tType "left" or "right"\n').lower()

if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    direction = input('\tType "wait" to wait for a boat. Type "swim" to swim '
                      'across.\n').lower()

    if direction == "wait":
        print("You've arrived at the island unharmed. There is a house with 3 doors.")
        direction = input("\tOne red, one yellow and one blue. Which color do you choose?\n").lower()

        if direction == "red":
            print("It's a room full of fire. \nGame over.")
        elif direction == "blue":
            print("You enter a room of beasts. \nGame over.")
        elif direction == "yellow":
            print("You found the treasure! \nYou win!")
        else:
            print("Game over.")

    elif direction == "swim":
        print("You get attacked by an angry trout. \nGame Over.")

    else:
        print("Game over.")
elif direction == "right":
    print("You fell into a hole. \nGame Over.")
else:
    print("Game Over.")

