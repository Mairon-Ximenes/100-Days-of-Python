import turtle
from operator import length_hint
from turtle import Screen
from turtle import Turtle
from paddle import Paddle

def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))

    screen.listen()
    
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")

    game_is_on = True
    while game_is_on:
        screen.update()


if __name__ == "__main__":
    main()