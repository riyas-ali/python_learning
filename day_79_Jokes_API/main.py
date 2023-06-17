import os
import time

import requests
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.get_database('mydatabase')
collection = 'jokes'
collection_names = db.list_collection_names()
if collection not in collection_names:
    db.create_collection(collection)
collection = db[collection]

while True:
    time.sleep(1)
    os.system('clear')
    result = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    joke = result.json()

    jk = joke["joke"]
    joke_id = joke["id"]
    print(jk)
    answer = input("N: Next\nL: Load\nS: Save\n:").lower()
    if answer == 'n':
        continue
    elif answer == 's':
        document = {'joke_id': joke_id}
        result = collection.insert_one(document)
        if result.acknowledged:
            print("\nSaved\n")
    elif answer == 'l':
        jokes = collection.find()
        for joke in jokes:
            result = requests.get(f'https://icanhazdadjoke.com/j/{joke["joke_id"]}', headers={'Accept': 'application/json'})
            joke_text = result.json()
            print(joke_text['joke'])
            time.sleep(3)