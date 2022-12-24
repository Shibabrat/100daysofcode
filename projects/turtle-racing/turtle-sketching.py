from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def rotate_ccw():
    tim.circle(100, 10)


def rotate_cw():
    tim.circle(100, -10)


def reset():
    screen.reset()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(rotate_ccw, "a")
screen.onkey(rotate_cw, "d")
screen.onkey(reset, "c")
screen.exitonclick()

