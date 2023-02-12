from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '_', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 5)
nr_numbers = random.randint(2, 5)

file_path = "/Users/OptimusPrime/"
file_name = "youshallnotpass"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    choice = [letters, numbers, symbols]
    password = [choice[random.randint(0, 2)][random.randint(0, len(choice) - 1)]
                for _ in range(nr_letters + nr_symbols + nr_numbers)]
    random.shuffle(password)
    password = "".join(password)

    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "Email": email,
            "Password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.askretrycancel(title="Incomplete form", message="Please don't leave any fields empty!")
    else:
        ready_to_save = messagebox.askokcancel(title = website,
                                               message = "Email: " + email + "\n"
                                                + "Password: " + password + "\n" + "Is this final?")

        if ready_to_save:
            with open(file_path + file_name + ".lotr", "a+") as file:
                file.write(website + " | " + email + " | " + password + "\n")

        if ready_to_save:
            try:
                with open(file_path + file_name + ".json", "r") as json_file:
                    data = json.load(json_file)
            except FileNotFoundError:
                print("File not found, creating new file.")
                with open(file_path + file_name + ".json", "w") as json_file:
                    json.dump(new_data, json_file, indent=4)
            else:
                # update the existing data with the new data
                data.update(new_data)

                with open(file_path + file_name + ".json", "w") as json_file:
                    # saving the updated data
                    json.dump(data, json_file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)

    return


# -------------------- SEARCH PASSWORD IN THE DATABASE------------------------------- #
def find_password():

    try:
        with open(file_path + file_name + ".json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print("No data file found")
    else:
        if website_entry.get() in data:
            email = data[website_entry.get()]['Email']
            password = data[website_entry.get()]['Password']
            messagebox.showinfo(title=f"Details for the {website_entry.get()}",
                                message = "Email: " + email + "\n"
                                          + "Password: " + password + "\n")
        else:
            messagebox.showinfo(title="Missing data",
                                message=f"No details for the website, {website_entry.get()}, exists.")

    return


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20)

canvas = Canvas(width = 200, height = 200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column = 1, row = 0)

# Labels
website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)

email_label = Label(text = "Email/Username:")
email_label.grid(column = 0, row = 2)

password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)

# Buttons
search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(column = 2, row = 1)

generate_button = Button(text="Generate Password", width = 11, command=generate_password)
generate_button.grid(column = 2, row = 3)

add_button = Button(text="Add", width = 34, command=save_password)
add_button.grid(column = 1, columnspan = 2, row = 4)

# Entries
website_entry = Entry(width = 21)
website_entry.grid(column = 1, columnspan = 1, row = 1)
website_entry.focus()

email_entry = Entry(width = 36)
email_entry.grid(column = 1, columnspan = 2, row = 2)
email_entry.insert(0, "shibabratnaik@gmail.com")

password_entry = Entry(width = 21)
password_entry.grid(column = 1, row = 3)

window.mainloop()
