from turtle import Turtle

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
EDGE_TOLERANCE = 5


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_velocity = 100
        self.y_velocity = 100
        self.time_elapsed = 0.1 # Increase speed of the ball with every hit

    def new_location(self):
        new_xcor = self.xcor() + self.x_velocity * self.time_elapsed
        new_ycor = self.ycor() + self.y_velocity * self.time_elapsed
        return new_xcor, new_ycor

    def move(self):
        new_xcor, new_ycor = self.new_location()
        self.goto(new_xcor, new_ycor)

    def bounce_wall(self):
        self.y_velocity *= -1
        new_xcor, new_ycor = self.new_location()
        self.goto(new_xcor, new_ycor)

    def bounce_paddle(self):
        self.x_velocity *= -1
        self.time_elapsed *= 1.05
        new_xcor, new_ycor = self.new_location()
        self.goto(new_xcor, new_ycor)

    def reset(self):
        self.goto(0, 0)
        self.time_elapsed = 0.1
        self.bounce_paddle()
        # self.color("white")
        # self.shape("circle")
        # self.penup()
        # self.x_velocity = -self.x_velocity
        # self.y_velocity = -self.y_velocity


