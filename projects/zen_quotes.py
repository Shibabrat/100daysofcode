from tkinter import *
import requests


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    quote = response.json()[0]["q"]
    author = response.json()[0]["a"]
    canvas.itemconfig(quote_text, text = quote + "\n\n" + author,
                      fill = "white", font = ("Ariel", 20, "bold"))
    pass


window = Tk()
window.title("Auto Zen says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

zen_quotes_img = PhotoImage(file="zen_quotes.png")
zen_quotes_button = Button(image=zen_quotes_img, highlightthickness=0, command=get_quote)
zen_quotes_button.grid(row=1, column=0)



window.mainloop()