import datetime as dt
import pandas
import random
import smtplib


MY_EMAIL = "naikpythondev@gmail.com"
MY_PASSWORD = "llxxwwvcgdperoax"  # app generated code
LETTER_TEMPLATE_PATH = "./letter_templates/"
NUM_TEMPLATES = 3

birthdays_data = pandas.read_csv("demo_birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays_data.iterrows()}

now = dt.datetime.now()
today_month_day = (now.month, now.day)

if today_month_day in birthdays_dict:

    birthday_person_data = birthdays_dict[today_month_day]
    print(birthday_person_data)

    filename = "letter_" + str(random.choice(range(1, NUM_TEMPLATES + 1))) + ".txt"
    with open(LETTER_TEMPLATE_PATH + filename) as letter_file:
        letter = letter_file.readlines()

    letter[0] = str(letter[0]).replace("[NAME]", birthday_person_data["name"])
    letter[-1] = str(letter[-1]).replace("Angela", "Shibabrat")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = birthday_person_data["email"],
            msg = "Subject:Best wishes\n\n" + ''.join(letter)
        )







