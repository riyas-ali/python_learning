import datetime
import os
import random
import time
import hashlib

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.get_database('mydatabase')
user_collection = db.get_collection('users')
collection_name = 'diaries'
collection_names = db.list_collection_names()
if collection_name not in collection_names:
    db.create_collection(collection_name)
diary_collection = db[collection_name]

username = None


def create_user():
    global username
    time.sleep(1)
    os.system("clear")
    username = input("Username: ")
    password = input("Password: ")
    check_duplicate = user_collection.find_one({"username": username})
    if check_duplicate:
        print(f"{username} is not available. You can proceed with the login.")
        return
    salt = random.randint(1000, 9999)
    new_password = f"{password}{salt}"
    hashed_password = generate_hash(new_password)
    document = {"username": username, "password": hashed_password, "salt": salt}
    result = user_collection.insert_one(document)
    if result.acknowledged:
        print("User added successfully")
    else:
        print("Error")
    time.sleep(1)
    os.system("clear")


def user_login():
    global username
    time.sleep(1)
    os.system("clear")
    username = input("Username: ")
    password = input("Password: ")

    existing_user = user_collection.find_one({"username": username})
    if existing_user:
        salt = existing_user["salt"]
        raw_password = f"{password}{salt}"
        hashed_password = generate_hash(raw_password)
        saved_password = existing_user["password"]
        if hashed_password == saved_password:
            print("Logged in")
            show_menu()
        else:
            print("Username or password incorrect")
    else:
        print(f"{username} is not available. You can create a new user.")
        return


def generate_hash(input_string):
    hash_object = hashlib.sha256()
    input_bytes = input_string.encode('utf-8')
    hash_object.update(input_bytes)
    hash_value = hash_object.hexdigest()
    return hash_value


def show_menu():
    while True:
        time.sleep(1)
        os.system("clear")
        print("--- Personal Diary ---")
        user_menu = input("1: Add\n2: View\n: ")
        if user_menu == "1":
            add()
        else:
            view()


def add():
    time.sleep(1)
    os.system("clear")
    time_stamp = datetime.datetime.now()
    print(time_stamp)
    diary = input(":- ")
    document = {"user": username, "date": time_stamp, "diary": diary}
    result = diary_collection.insert_one(document)
    if result.acknowledged:
        print("Added Successfully")
    else:
        print("Error")


def view():
    time.sleep(1)
    os.system("clear")
    diary_entries = diary_collection.find({"user": username})
    count = 0
    for diary in diary_entries:
        print(diary["date"])
        print(diary["diary"])
        count += 1
        if count % 10 == 0:
            carry_on = input("Next 10?: ")
            if carry_on.lower() == "no":
                break
    time.sleep(2)
    os.system("clear")


while True:
    print("--- Personal Diary ---")
    menu = input("1: New User\n2: Login\n: ")
    if menu == "1":
        create_user()
    else:
        user_login()
