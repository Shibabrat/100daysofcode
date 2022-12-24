from turtle import Turtle, Screen
from random import choice, randint
from prettytable import PrettyTable

colors = ["DarkGreen", "DeepSkyBlue", "Red", "Purple",
          "DarkOrchid", "MediumSeaGreen", "SaddleBrown",
          "SeaGreen"]


def random_color():

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color = (r, g, b)

    return color


my_screen = Screen()
my_screen.colormode(255)

tim = Turtle()
# print(timmy)
tim.shape("turtle")
tim.color("blue")

# Drawing a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Drawing a dashed line
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# Drawing n-gons with different colors
# for i in range(3, 11):
#     angle = 360 / i
#     tim.color(choice(colors))
#     for _ in range(i):
#         tim.forward(100)
#         tim.right(angle)


# Generating random walk
# walk_step = 40
# tim.pensize(20)
# tim.speed("fast")
# for _ in range(50):
#     walk_angle = choice(range(0, 450, 90))
#     # tim.color('#%06X' % choice(range(0xFFFFFF)))
#     tim.color(random_color())
#     if choice(["left", "right"]) == "left":
#         tim.left(walk_angle)
#     else:
#         tim.right(walk_angle)
#
#     tim.forward(walk_step)

# Draw a spirograph
tim.speed("fastest")


def draw_spirograph(num_circles):
    for i in range(num_circles):
        angle = (i * 360 / num_circles)
        tim.setheading(angle)
        tim.color(random_color())
        tim.circle(100, 360, 100)


draw_spirograph(100)

# print(my_screen.canvheight)
my_screen.exitonclick()

# table = PrettyTable()
# table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
#
# print(table)
