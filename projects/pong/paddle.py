from turtle import Turtle

CANVAS_WIDTH = 800
EDGE_TOLERANCE = 40
UP = 90
DOWN = 270
STEP_LENGTH = 20


class Paddle(Turtle):

    def __init__(self, side=-1):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(side*CANVAS_WIDTH/2, 0)

    def up(self):
        self.goto(self.xcor(), self.ycor() + STEP_LENGTH)

    def down(self):
        self.goto(self.xcor(), self.ycor() - STEP_LENGTH)



