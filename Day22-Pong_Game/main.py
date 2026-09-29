import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if (ball.distance(r_paddle) < 45 and ball.xcor() > 320) or (ball.distance(l_paddle) < 45 and ball.xcor() < -320):
            ball.bounce_x()
            ball.accelerate()

        if ball.xcor() > 380 or ball.xcor() < -380:
            if ball.xcor() > 380: scoreboard.l_point()
            elif ball.xcor() < -380: scoreboard.r_point()
            ball.reset_position()
            l_paddle.reset_position()
            r_paddle.reset_position()
            time.sleep(0.5)








if __name__ == "__main__":
    main()