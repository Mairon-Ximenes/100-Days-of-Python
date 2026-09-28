from turtle import Turtle
X_POSITION = 350

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(350, 0)
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)