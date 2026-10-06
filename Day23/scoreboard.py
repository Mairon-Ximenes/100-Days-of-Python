from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.level = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.goto(-230, 250)
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align=ALIGN, font=FONT)

