from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

try:
    french_words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words = pandas.read_csv("data/french_words.csv")
    words_to_learn = french_words.to_dict(orient = "records")
else:
    words_to_learn = french_words.to_dict(orient = "records")

new_word = {}


# ---------------------------- SAVE PROGRESS ------------------------------------- #
def save_known_words():

    words_to_learn.remove(new_word)
    if len(words_to_learn) == 0:
        print("Congrats you have learnt all the words in the imported list")
        window.quit()
    else:
        dataframe = pandas.DataFrame(words_to_learn)
        dataframe.to_csv("data/words_to_learn.csv", index=False)
        generate_word()


# ---------------------------- FLIP CARD TO REVEAL ------------------------------- #
def flip_card():
    canvas.itemconfig(card_background, image=back_img)

    canvas.itemconfig(card_title, text="English", fill="white", font=("Ariel", 40, "italic"))

    canvas.itemconfig(card_word, text=new_word["English"], fill="white", font=("Ariel", 60, "bold"))


# ---------------------------- GENERATE NEW WORDS ------------------------------- #
def generate_word():
    global new_word, flip_timer
    window.after_cancel(flip_timer)  # invalidate the global flip timer

    new_word = random.choice(words_to_learn)

    canvas.itemconfig(card_word, text=new_word["French"],
                      fill="black", font=("Ariel", 60, "bold"))
    canvas.itemconfig(card_background, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black", font=("Ariel", 40, "italic"))

    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(width=800, height=800,
              bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file = "images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text= "", fill= "black", font=("Ariel", 60, "bold"))
canvas.grid(column = 0, columnspan=2, row = 0)

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, width=97, bg=BACKGROUND_COLOR,
                      highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, width=97, bg=BACKGROUND_COLOR,
                      highlightthickness=0, command=save_known_words)
right_button.grid(column=1, row=1)

generate_word()

window.mainloop()
