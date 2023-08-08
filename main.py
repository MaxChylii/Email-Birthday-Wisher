import datetime as dt
import smtplib
import pandas
import random

MY_EMAIL = "YOUR @GMAIL"
MY_PASSWORD = "YOUR PASSWORD"

# Check if someone in the birthday.csv have a birthday today
now = dt.datetime.now()
month = now.month
day = now.day

bd = pandas.read_csv("birthdays.csv")
b_month = bd[bd.month == month]
b_day = b_month[b_month.day == day]
b_name = []

# If YES choose the random letter, change [NAME], and send the happy birthday email
if len(b_month) != 0 and len(b_day) != 0:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)

    for name in b_day.name:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as wish:
            b_wish = wish.read().replace("[NAME]", name)

        b_email = b_day[b_day["name"] == name].email
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=b_email,
            msg=f"Subject:Happy Birthday\n\n{b_wish}"
        )
    connection.close()
