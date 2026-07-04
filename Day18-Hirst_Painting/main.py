from turtle import Turtle, Screen
from list_tuples import list_tuples_rgb
import random, turtle

def go_to_start(t, steps):
    t.setheading(225)
    t.forward(steps)
    t.setheading(0)


def go_to_beggining(t: Turtle, steps: int):
    t.forward(steps)
    t.setheading(0)


def main():
    turtle.colormode(255)
    print(list_tuples_rgb)
    t = Turtle()

    t.width(15)
    t.penup()
    t.hideturtle()
    
    go_to_start(t, 325)
    number_of_dots = 100
    t.speed('fastest')

    for i in range(1, number_of_dots + 1):
        t.dot(20, random.choice(list_tuples_rgb))
        t.forward(50)

        if i % 10 == 0:
            t.left(90)
            t.forward(50)
            t.left(90)
            go_to_beggining(t, 50 * 10)




    screen = Screen()
    screen.exitonclick()


main()
