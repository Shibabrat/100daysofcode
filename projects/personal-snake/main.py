"""
Snake game that remembers all the high score and shows the most recent one during play
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CLOSE_TO_WALL = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# screen.onkey(.bye(), "q")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food) < 20:
        food.refresh()
        scoreboard.hit()
        snake.extend()

    # Detect collision with wall
    if math.fabs(snake.segments[0].xcor()) > SCREEN_WIDTH/2 - CLOSE_TO_WALL or \
            math.fabs(snake.segments[0].ycor()) > SCREEN_HEIGHT/2 - CLOSE_TO_WALL:
        scoreboard.restart()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 1:
            scoreboard.restart()
            snake.reset()

screen.exitonclick()


