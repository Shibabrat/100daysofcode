from turtle import Turtle, Screen, colormode
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
TIME_ELAPSED = 0.1

screen = Screen()
screen.screensize(canvwidth=CANVAS_WIDTH, canvheight=CANVAS_HEIGHT, bg="black")

# TODO: 1. Prepare the display

turtle = Turtle()

colormode(255)
turtle.hideturtle()
turtle.penup()
turtle.goto(0, CANVAS_HEIGHT / 2)
turtle.pencolor("white")
turtle.pensize(10)
turtle.speed("fastest")
screen.tracer(0)


score_left = Scoreboard(side=-1)
score_right = Scoreboard(side=1)

# TODO: 2. Add the paddles and control the paddles
paddle_left = Paddle(side=-1)  # -1: left side, 1: right side
paddle_right = Paddle(side=1)

screen.listen()
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")

# TODO: 4. Add the ball and animate
ball = Ball()

game_on = True
while game_on:
    time.sleep(ball.time_elapsed)
    screen.update()
    ball.move()

    # TODO: 4b. Detect collisions with the top and bottom wall
    if ball.ycor() > CANVAS_HEIGHT/2 - 20 or ball.ycor() < -CANVAS_HEIGHT/2 + 20:
        # print("Collision with the top wall")
        ball.bounce_wall()

    # TODO: 5. Detect ball touching the paddles or missing the paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > CANVAS_WIDTH/2 - 20:
        ball.bounce_paddle()
    elif ball.distance(paddle_left) < 50 and ball.xcor() > -CANVAS_WIDTH/2 + 20:
        ball.bounce_paddle()

    # TODO: 6. Add the scoreboard, net, and update score, game ends when one
    #  side reaches 15
    if ball.xcor() > CANVAS_WIDTH/2:
        ball.reset()
        score_left.score()

    if ball.xcor() < -CANVAS_WIDTH/2:
        ball.reset()
        score_right.score()

    # if int(score_left.score()) > 1 or int(score_right.score()) > 1:
    #     game_on = False


screen.exitonclick()

