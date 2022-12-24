# SECOND CAPSTONE PROJECT
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from math import fabs
from random import randint

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FINISH_LINE = SCREEN_HEIGHT/2 - 100

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle crossing")
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

car_manager = []

game_is_on = True
while game_is_on:
    time.sleep(0.7)

    random_car_birth = randint(1, 6)
    if random_car_birth == 1:
        car = CarManager()
        car_manager.append(car)

    for i in range(len(car_manager)):
        car_manager[i].move()
        if car_manager[i].distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # if car_manager[i].position()[0] < -300:
    #     car_manager.pop(i)

    screen.update()

    if player.finished_level():
        scoreboard.level_up()
        for car in car_manager:
            car.level_up()
        player.restart()


screen.exitonclick()


# TODO: 3. Detect collision with a car (still buggy), change car speed with level.


