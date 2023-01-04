from turtle import Turtle
import os

PATH_HIGH_SCORE_FILE = "./high_score.txt"

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

        if os.path.isfile(PATH_HIGH_SCORE_FILE):
            with open(PATH_HIGH_SCORE_FILE, "r+") as file:
                self.high_score = int(file.read())

        self.write_score()

    def update_scoreboard(self):
        self.clear()
        self.write_score()

    def hit(self):
        self.value += 1
        self.update_scoreboard()

    def restart(self):
        if self.value > self.high_score:
            self.high_score = self.value
        self.save_high_score()

        self.value = 0
        self.update_scoreboard()

    def write_score(self):
        self.write(f"Score: {self.value}. High score: {self.high_score}", align=ALIGNMENT,
                   font=FONT)

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(f"{self.high_score}")

