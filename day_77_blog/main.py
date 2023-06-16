from flask import Flask, redirect, session, request, render_template
from pymongo import MongoClient
import secrets
import hashlib

client = MongoClient('mongodb://localhost:27017/')
db = client.get_database('mydatabase')
collection = db.get_collection('users')
collection_name = 'blogs'
collection_names = db.list_collection_names()
if collection_name not in collection_names:
    db.create_collection(collection_name)
blog_collection = db[collection_name]

app = Flask(__name__, static_url_path='/static')
app.secret_key = secrets.token_hex(16)


@app.route('/')
def index():
    if session.get('logged_in'):
        return redirect('/edit')
    return render_template('blog.html', blogs=get_blogs())


@app.route('/loginForm')
def login_form():
    if session.get('logged_in'):
        return redirect('/edit')
    return render_template('login.html')


def generate_hash(input_string):
    hash_object = hashlib.sha256()
    input_bytes = input_string.encode('utf-8')
    hash_object.update(input_bytes)
    hash_value = hash_object.hexdigest()
    return hash_value


@app.route('/login', methods=['POST'])
def login():
    if session.get('logged_in'):
        return redirect('/edit')
    form = request.form
    existing_user = collection.find_one({'username': form['username']})
    if existing_user:
        salt = existing_user['salt']
        raw_password = f"{form['password']}{salt}"
        hashed_password = generate_hash(raw_password)
        saved_password = existing_user['password']
        if hashed_password == saved_password:
            session['logged_in'] = form['username']
            return redirect('/edit')
        else:
            return redirect('/loginForm')
    else:
        return redirect('/loginForm')


def get_blogs():
    blogs = blog_collection.find()
    blog_entries = []
    for blog in blogs:
        entry = {
            'title': blog['title'],
            'date': blog['date'],
            'body': blog['body']
        }
        blog_entries.append(entry)
    return reversed(blog_entries)


@app.route('/edit')
def edit():
    if not session.get('logged_in'):
        return redirect('/')
    return render_template('edit.html', blogs=get_blogs())


@app.route('/add', methods=['POST'])
def add():
    form = request.form
    entry = {'title': form['title'], 'date': form['date'], 'body': form['body']}
    result = blog_collection.insert_one(entry)
    return redirect('/edit')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(host='0.0.0.0', port=8080)
