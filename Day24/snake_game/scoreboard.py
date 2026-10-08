from turtle import Turtle
ALIGNMENT = "center"
FONT_SIZE = 15
FONT = ('Arial', FONT_SIZE, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0, y=270)
        self.penup()
        self.score = 0
        with open('high_score.txt', 'r') as data:
            self.high_score = int(data.read())

        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()