# TODO: 1. Create a snake body
#       2a. Move the snake
#       2b. Create a class for snake, food, scoreboard
#       3. Control the snake
#       4. Detect collision with food
#       5. Create a scoreboard
#       6. Detect collision with wall
#       7. Detect collision with tail

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
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 1:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()


