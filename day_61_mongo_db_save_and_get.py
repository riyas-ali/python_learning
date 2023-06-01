import datetime
import os
import time

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.get_database('mydatabase')
collection = db.get_collection('mycollection')


def add_tweet():
    tweet = input("👉️: ")
    time_stamp = datetime.datetime.now()
    key = f"mes{time_stamp}"
    document = {key: tweet}
    result = collection.insert_one(document)
    if result.acknowledged:
        print("Item added successfully")
    else:
        print("Error")
    time.sleep(1)
    os.system("clear")


def view_tweet():
    result = collection.find()
    msgs_all = []
    for document in result:
        values = document.values()
        msgs = (list(values))
        msgs_all.append(msgs[1])
    msgs_all.reverse()
    counter = 0
    for msg in msgs_all:
        print(msg)
        counter += 1
        if counter % 10 == 0:
            carry_on = input("Next 10?: ")
            if carry_on.lower() == "no":
                break
    time.sleep(2)
    os.system("clear")


while True:
    print("Tweeter")
    menu = input("1: Add Tweets\n2: View Tweets\n: ")
    if menu == "1":
        add_tweet()
    else:
        view_tweet()