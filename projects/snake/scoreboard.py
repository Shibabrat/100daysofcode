from turtle import Turtle

SCREEN_HEIGHT = 600
EDGE_TOLERANCE = 40

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.value = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, SCREEN_HEIGHT/2 - EDGE_TOLERANCE)
        self.write(f"Score: {self.value}", align=ALIGNMENT,
                   font=FONT)

    def hit(self):
        self.value += 1
        self.clear()
        self.write(f"Score: {self.value}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT,
                   font=FONT)



