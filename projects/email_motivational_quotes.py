import smtplib
import datetime as dt
import random

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

my_email = "naikpythondev@gmail.com"
my_password = "llxxwwvcgdperoax"  # app generated code

now = dt.datetime.now()

if now.weekday() == 2:  # Monday: 0
    with open("quotes.txt", "r") as file:
        list_quotes = file.readlines()

    motivational_quote = random.choice(list_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = my_password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = "shibabratn@yahoo.com",
            msg = "Subject:Motivational " + WEEKDAYS[now.weekday()] + "s by Naik \n\n"
                  + motivational_quote
        )