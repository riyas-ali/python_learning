import time
import requests, schedule, os
from bs4 import BeautifulSoup
from bson import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

username = os.getenv('MAIL_USERNAME')
password = os.getenv('MAIL_PASSWORD')

client = MongoClient('mongodb://localhost:27017/')
db = client.mydatabase
collection = db['price_tracker']


def add_to_db():
    link = input("Link: ")
    price = float(input("price: "))
    new_data = {
        'link': link,
        'price': None,
        'level': price,
    }
    collection.insert_one(new_data)


# add_to_db()
def mail_to_me(level, price, link):
    email = f'<p><a href="{link}">This product</a> is now ${price} which is below your purchase level of ${level}</p>'
    server = 'smtp.gmail.com'
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg['To'] = 'riyasmonokl@gmail.com'
    msg['From'] = username
    msg['Subject'] = "Product is Cheaper"
    msg.attach(MIMEText(email, 'html'))
    s.send_message(msg)
    del msg


def update():
    datas = collection.find()
    for data in datas:
        url = data['link']
        price = data['price']
        level = data['level']

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        my_price = soup.find_all('span', {'class': 'price wex-red'})
        price_of = float(my_price[0].text[1:8].replace(',', ''))
        if price_of != price:
            collection.update_one(
                {'_id': ObjectId(data['_id'])},
                {'$set': {'price': price_of}}
            )
        if price_of <= level:
            mail_to_me(level, price, url)


schedule.every(1).day.do(update())

while True:
    schedule.run_pending()
    time.sleep(1)
