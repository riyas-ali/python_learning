import os, random
import time
from dotenv import load_dotenv
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

username = os.getenv('MAIL_USERNAME')
password = os.getenv('MAIL_PASSWORD')

with open('quotes.txt', 'r') as file:
    quotes = file.readlines()
file.close()

quote = random.choice(quotes)


def send_mail():
    email = quote
    server = 'smtp.gmail.com'
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg['To'] = 'riyasmonokl@gmail.com'
    msg['From'] = username
    msg['Subject'] = "Daily Quote"
    msg.attach(MIMEText(email, 'html'))

    s.send_message(msg)
    del msg


def job():
    send_mail()


schedule.every(24).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
