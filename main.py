import smtplib
import random
import datetime as dt
from pathlib import Path

now = dt.datetime.now()

###Learning abt datetime
year = now.year
#print(f"Party like it's {year}!")
#dob = dt.datetime(year=1997, month=6, day=12)

#TODO ========= Motivational quote email project ===========
q = open('quotes.txt', 'r')
quotes = q.readlines() #quotes is a list type
random_quote = random.choice(quotes)

GMAIL = "dummy@GMAIL.com"
GMAIL_PW = "dummypw"

# if day==4: #set it for today
#     with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as connection:
#         # this statement automatically closes off the connection once the email has been sent
#         connection.starttls()  # makes connection secure
#         connection.login(user = GMAIL, password = GMAIL_PW)
#         connection.sendmail(
#             from_addr = GMAIL,
#             to_addrs = "dummy@yahoo.com.sg",
#             msg = f"Subject: Motivational quote of the day\n\n{random_quote}")


#TODO ============= Birthday Wisher Hard Starting Project ================

import pandas
df = pandas.read_csv("birthdays.csv")

# Check if today matches a birthday in the birthdays.csv
today = (now.month, now.day)

# Create a dictionary from birthdays.csv. The key is going to be a tuple of (month,day)
#https://www.askpython.com/python-modules/pandas/dataframe-rows-and-columns
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today in birthdays_dict:
    birthday_kid = birthdays_dict[today]["name"]
    random_template = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(random_template) as l:
        ltr = l.read()
        letter = ltr.replace("[NAME]", birthday_kid) #Swap out placeholder
        print(letter)
    with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as connection: #this statement automatically closes off the connection once the email has been sent
        connection.starttls()  # makes connection secure
        connection.login(user = GMAIL, password = GMAIL_PW)
        connection.sendmail(
            from_addr = GMAIL,
            to_addrs = birthdays_dict[today]["email"],
            msg = f"Subject: Happee Burfdae!\n\n{letter}"
            )
        
#Can upload to pythonanywhere for autorefresh/to check whether any bday emails need to be sent daily


