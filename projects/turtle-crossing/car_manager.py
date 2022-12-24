from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_SPEED = 20
MOVE_INCREMENT = 10
TIME_ELAPSED = 1.0
SCREEN_WIDTH = 600


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color(choice(COLORS))
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(SCREEN_WIDTH/2 - 50, randint(-200, 200))
        self.speed = STARTING_MOVE_SPEED

    def move(self):
        self.goto(self.xcor() - self.speed * TIME_ELAPSED, self.ycor())

    def level_up(self):
        self.speed += MOVE_INCREMENT



