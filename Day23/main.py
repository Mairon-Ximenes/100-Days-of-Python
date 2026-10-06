import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()

    screen.onkey(player.move, "Up")
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        num = random.randint(1, 6)

        if num == 1:
            car_manager.create_car()
        car_manager.move_cars()

        for car in car_manager.cars:
            if car.distance(player) <= 25:
                scoreboard.game_over()
                screen.update()
                screen.exitonclick()
                game_is_on = False

        if player.is_at_finish_line():
            player.go_to_start_position()
            scoreboard.update_scoreboard()
            car_manager.level_up()


if __name__ == "__main__":
    main()