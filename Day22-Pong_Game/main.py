import turtle
from operator import length_hint
from turtle import Screen
from turtle import Turtle
from paddle1 import Paddle

def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    paddle1 = Paddle()

    screen.listen()
    
    screen.onkey(paddle1.move_up, "Up")
    screen.onkey(paddle1.move_down, "Down")

    while True:
        screen.update()


if __name__ == "__main__":
    main()