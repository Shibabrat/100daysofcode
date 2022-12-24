from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POSITION)

    def finished_level(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
