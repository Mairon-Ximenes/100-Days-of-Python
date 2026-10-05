from turtle import Turtle
import random

from Day23.player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_len=2, stretch_wid=1)

        car.y = random.randint(-270, 250)
        car.goto(300, car.y)
        self.cars.append(car)

    def check_colision(self, player: Player):
        for car in self.cars:
            if car.distance(player) <= 25:
                return True
        return False

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - self.move_distance, car.ycor())

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

    def level_up(self):
        self.increase_speed()
        for car in self.cars:
            car.hideturtle()

        self.cars.clear()