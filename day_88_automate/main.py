import os
import time
from dotenv import load_dotenv
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

username = os.getenv('MAIL_USERNAME')
password = os.getenv('MAIL_PASSWORD')


def send_mail():
    email = "Don't forgot to take a break!"
    server = 'smtp.gmail.com'
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg['To'] = 'riyasmonokl@gmail.com'
    msg['From'] = username
    msg['Subject'] = "Take a break!"
    msg.attach(MIMEText(email, 'html'))

    s.send_message(msg)
    del msg


def job():
    send_mail()


schedule.every(1).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
