##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import pandas
import random
import smtplib
my_email = "testgmail204@gmail.com"
password = "ijsdirgfggflxstg"
letter = random.randint(1,3)
birthday = pandas.read_csv("birthdays.csv")
month_values = birthday['month'].to_list()
day_values = birthday['day'].to_list()
name_values = birthday['name'].to_list()
email_values = birthday['email'].to_list()
now = dt.datetime.now()
day = now.day
month = now.month
num = 0
for person in range(len(month_values)):
    if month_values[person] == month:
        if day_values[person] == day:
            with open(f"letter_{letter}.txt") as file:
                content = file.read()
                contents = str(content)
                invited_person = contents.replace("[NAME]", f"{name_values[person]}")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user = my_email,password = password)
                connection.sendmail(from_addr=my_email, to_addrs=f"{email_values[person]}", msg="Subject:Happy birthday\n\n"
                                                                                                  f"{invited_person}")












