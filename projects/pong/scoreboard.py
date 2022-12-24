from turtle import Turtle

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
EDGE_TOLERANCE = 40

ALIGNMENT = "center"
FONT = ("Courier", 100, "normal")


class Scoreboard(Turtle):

    def __init__(self, side=-1):
        super().__init__()
        self.value = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(side*2*EDGE_TOLERANCE, CANVAS_HEIGHT/2)
        self.write(f"{self.value}", align=ALIGNMENT, font=FONT)

        # y = CANVAS_HEIGHT / 2
        # while y > -CANVAS_HEIGHT / 2:
        #     self.pendown()
        #     y -= 20
        #     self.goto(0, y)
        #     self.penup()
        #     y -= 40
        #     self.goto(0, y)

    def score(self):
        self.value += 1
        self.clear()
        self.write(f"{self.value}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT,
                   font=FONT)

