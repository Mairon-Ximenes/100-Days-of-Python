import random
from _pyrepl import commands
from turtle import Turtle, Screen


def main():

    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = (screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: '))

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    all_turtles = []

    for turtle_index in range(6):
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-230, y=-75 + (30 * turtle_index))
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    winner_color = ''
    while is_race_on:
        for turtle in all_turtles:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

            if turtle.xcor() >= 230:
                is_race_on = False
                winner_color = turtle.pencolor()
                if winner_color == user_bet:
                    print(f"You've won! The {winner_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winner_color} turtle is the winner!")


    screen.exitonclick()


main()