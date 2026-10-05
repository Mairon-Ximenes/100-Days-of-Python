import time
from turtle import Screen

from Day23 import scoreboard
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
    counter = 0
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        if counter == 6:
            car_manager.create_car()
            counter = 0
        car_manager.move_cars()

        if car_manager.check_colision(player):
            scoreboard.game_over()
            screen.update()
            screen.exitonclick()
            game_is_on = False


        if player.distance(0, 300) <= 20:
            player.reset()
            scoreboard.update_scoreboard()
            car_manager.level_up()

        counter += 1





if __name__ == "__main__":
    main()