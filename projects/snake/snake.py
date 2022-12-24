from turtle import Turtle

STEP_LENGTH = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.segments.append(Turtle("square"))
            self.segments[i].color("white")
            self.segments[i].penup()
            self.segments[i].setposition(-40 + (2 - i) * 20, 0)

    def extend(self):
        self.segments.append(Turtle("square"))
        self.segments[-1].color("white")
        self.segments[-1].penup()
        self.segments[-1].setposition(self.segments[-2].position()[0] + 20,
                                      self.segments[-2].position()[1])

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position()[0],
                                  self.segments[i - 1].position()[1])
        self.segments[0].forward(STEP_LENGTH)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

