from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.original_coordinates = coordinates
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.original_coordinates)
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y <= 275:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y >= -255:
            self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(self.original_coordinates)