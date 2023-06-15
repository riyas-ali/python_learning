from flask import Flask, request, redirect, session
from pymongo import MongoClient
import random
import hashlib
import secrets

client = MongoClient('mongodb://localhost:27017/')
db = client.get_database('mydatabase')
collection = db.get_collection('users')

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route('/')
def index():
    if session.get('logged_in'):
        return redirect('/welcome')
    page = """<p><a href="/signup">Signup</a></p><p><a href="/login">Login</a></p>"""
    return page


def generate_hash(input_string):
    hash_object = hashlib.sha256()
    input_bytes = input_string.encode('utf-8')
    hash_object.update(input_bytes)
    hash_value = hash_object.hexdigest()
    return hash_value


@app.route('/signup')
def signup():
    if session.get('logged_in'):
        return redirect('/welcome')
    f = open('template/signup.html', 'r')
    page = f.read()
    f.close()
    return page


@app.route('/signup', methods=['POST'])
def create_user():
    if session.get('logged_in'):
        return redirect('/welcome')
    form = request.form
    check_duplicate = collection.find_one({"username": form['username']})
    if check_duplicate:
        print(f"{form['username']} is available. You can proceed another username.")
        return redirect('/signup')
    else:
        salt = random.randint(1000, 9999)
        new_password = f"{form['password']}{salt}"
        hashed_password = generate_hash(new_password)
        document = {"username": form['username'], "password": hashed_password, "salt": salt}
        result = collection.insert_one(document)
        if result.acknowledged:
            print("User added successfully")
            return redirect('/login')
        else:
            print("Error")


@app.route('/login')
def login():
    if session.get('logged_in'):
        return redirect('/welcome')
    f = open('template/login.html', 'r')
    page = f.read()
    f.close()
    return page


@app.route('/login', methods=['POST'])
def login_user():
    if session.get('logged_in'):
        return redirect('/welcome')
    form = request.form
    existing_user = collection.find_one({"username": form['username']})
    if existing_user:
        salt = existing_user["salt"]
        raw_password = f"{form['password']}{salt}"
        hashed_password = generate_hash(raw_password)
        saved_password = existing_user["password"]
        if hashed_password == saved_password:
            print("Logged in")
            session['logged_in'] = form['username']
            return redirect('/welcome')
        else:
            print("Username or password incorrect")
            return redirect('/login')
    else:
        print(f"{form['username']} is not available. You can create a new user.")
        return redirect('/login')


@app.route('/welcome')
def welcome():
    page = f'''<h1>Hi there {session["logged_in"]}</h1>
            <button type="button" onclick=location.href="/logout">Logout</button>'''
    return page


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(host='0.0.0.0', port=8080)
