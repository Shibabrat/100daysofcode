from turtle import Turtle
from random import uniform

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
EDGE_TOLERANCE = 40


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        x_location = uniform(-SCREEN_WIDTH/2 + 40,
                             SCREEN_WIDTH/2 - 40)
        y_location = uniform(-SCREEN_HEIGHT/2 + 40,
                             SCREEN_HEIGHT/2 - 40)
        self.goto(x_location, y_location)

    def refresh(self):
        x_location = uniform(-SCREEN_WIDTH / 2 + 40,
                             SCREEN_WIDTH / 2 - 40)
        y_location = uniform(-SCREEN_HEIGHT / 2 + 40,
                             SCREEN_HEIGHT / 2 - 40)
        self.goto(x_location, y_location)