from turtle import Turtle, Screen
from random import choice
# import colorgram
#
# colors = colorgram.extract("spot-painting2.jpg", 10)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_colors.append((r, g, b))
#
#
# print(rgb_colors)
# color_list = [(229, 228, 227), (226, 224, 225), (198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56)]
color_list = [(194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34),
              (198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56)]


def goto_nextline(tim):
    """Moves the turtle to the next line above
    """
    tim.setheading(180)
    tim.forward(spot_spacing * num_spots_xdir)
    tim.right(90)
    tim.forward(spot_spacing)
    tim.right(90)

    return tim


spot_size = 20
spot_spacing = 50
num_spots_xdir = 10
num_spots_ydir = 10

tim = Turtle()
screen = Screen()
screen.title("Welcome to my tutle painting a Damien Hirst!")
# screen.setup(width=0.5, height=0.5, startx=None, starty=None)

screen.colormode(255)
tim.speed("fastest")
tim.hideturtle()
tim.penup()

tim.left(180)
tim.forward(spot_spacing*num_spots_xdir/2)
tim.left(90)
tim.forward(spot_spacing*num_spots_ydir/2)
tim.left(90)

for _ in range(num_spots_ydir):
    for _ in range(num_spots_xdir):
        tim.dot(spot_size, color_list[choice(range(0, len(color_list)))])
        tim.forward(spot_spacing)

    tim = goto_nextline(tim)

screen.exitonclick()


