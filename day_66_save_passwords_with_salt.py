import os
import random
import time
import hashlib

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.get_database('mydatabase')
collection = db.get_collection('users')


def create_user():
    time.sleep(1)
    os.system("clear")
    username = input("Username: ")
    password = input("Password: ")
    check_duplicate = collection.find_one({"username": username})
    if check_duplicate:
        print(f"{username} is available. You can proceed with the login.")
        return
    salt = random.randint(1000, 9999)
    new_password = f"{password}{salt}"
    hashed_password = generate_hash(new_password)
    document = {"username": username, "password": hashed_password, "salt": salt}
    result = collection.insert_one(document)
    if result.acknowledged:
        print("User added successfully")
    else:
        print("Error")
    time.sleep(1)
    os.system("clear")


def user_login():
    time.sleep(1)
    os.system("clear")
    username = input("Username: ")
    password = input("Password: ")

    existing_user = collection.find_one({"username": username})
    if existing_user:
        salt = existing_user["salt"]
        raw_password = f"{password}{salt}"
        hashed_password = generate_hash(raw_password)
        saved_password = existing_user["password"]
        if hashed_password == saved_password:
            print("Logged in")
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


while True:
    menu = input("1: New User\n2: Login\n: ")
    if menu == "1":
        create_user()
    else:
        user_login()