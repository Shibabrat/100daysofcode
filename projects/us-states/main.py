import pandas
from turtle import Screen, Turtle

states_screen = Screen()
states_screen.setup(width=800, height=800)
states_screen.title("US states games")
states_screen.addshape("blank_states_img.gif")

states_turtle = Turtle()
states_turtle.shape("blank_states_img.gif")

writer_turtle = Turtle()
writer_turtle.hideturtle()
writer_turtle.penup()

states = pandas.read_csv("50_states.csv")

states_names = states["state"].to_list()
i = 1
while i <= 50:
    answer_state = states_screen.textinput(title=f"{i}/50 states correct",
                                           prompt="What's another state's name?")

    check_state_name = answer_state.lower() == states["state"].str.lower()

    if check_state_name.any():
        writer_turtle.goto(float(states[check_state_name]['x']),
                           float(states[check_state_name]['y']))
        writer_turtle.write(states[check_state_name]['state'].item(),
                            align="center",
                            font=("Courier", 16, "normal"))

        states_names.pop(answer_state.lower() == states_names)

        i = i + 1

    if answer_state.lower() == "exit":
        break


data_dict = {
    "State": states_names,
}
data_save = pandas.DataFrame(data_dict)
data_save.to_csv("missed_states.csv")

states_screen.exitonclick()
