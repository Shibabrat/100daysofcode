from turtle import Turtle, Screen
from random import uniform

screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color from VIBGYOR")

tim_red = Turtle()
tim_orange = Turtle()
tim_yellow = Turtle()
tim_green = Turtle()
tim_blue = Turtle()
tim_indigo = Turtle()
tim_violet = Turtle()

racers = [tim_red, tim_orange, tim_yellow, tim_green, tim_blue,
          tim_indigo, tim_violet]

color = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]


def get_set_turtles(tim, starting_position):

    tim.color(color[starting_position-1])
    tim.shape("turtle")
    tim.penup()
    tim.goto(x=-400, y=350 - starting_position * 100)


# Set starting position for the turtles
for i in range(len(racers)):
    get_set_turtles(racers[i], i + 1)

race_finished = False
turtles_ranking = []
while not race_finished:
    for k in range(len(racers)):
        if racers[k].position()[0] < 400:
            racers[k].setposition(racers[k].position()[0] + uniform(0, 40), racers[k].position()[1])

            if racers[k].position()[0] >= 400:
                racers[k].setposition(400, racers[k].position()[1])
                print(f"{color[k]} turtle finished")
                turtles_ranking.append(color[k])

    if len(turtles_ranking) == 7:
        race_finished = True

if user_bet.lower() == turtles_ranking[0].lower():
    print("You win!")
else:
    print(f"You lose, {turtles_ranking[0]} turtle won the race")


screen.exitonclick()






