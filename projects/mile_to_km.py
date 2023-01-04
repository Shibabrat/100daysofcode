from tkinter import *


def mile_to_km():
    miles_to_convert = float(input_miles.get())
    label3.config(text=f"{miles_to_convert * 1.609:.3f}")


# Creating a new window and configurations
window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)
# Labels
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)

label2 = Label(text="Km")
label2.grid(column=2, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

# Text
input_miles = Entry(width=10, borderwidth=5)
input_miles.grid(column=1, row=0)
# Add some text to begin with
input_miles.insert(END, string="0")


# Button
button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()
