from flask import Flask, request

app = Flask(__name__)

logins = {"riyas": {"email": "a@test.com", "password": "test123"},
          "ashiq": {"email": "b@test.com", "password": "test456"},
          "uwais": {"email": "c@test.com", "password": "test789"}}


@app.route("/login", methods=["POST"])
def login():
    form = request.form
    is_there = False
    details = {}
    try:
        details = logins[form["username"]]
        is_there = True
    except:
        return "Username, email or password incorrect"

    if form["email"] == details['email'] and form['password'] == details['password']:
        return "You are logged in"
    else:
        return "Username, email or password incorrect"


@app.route('/')
def index():
    page = '''
    <form method="post" action="/login">
    <p>Username: <input type="text" name="username" required></p>
    <p>Email: <input type="email" name="email" required></p>
    <p>Password: <input type="password" name="password" required></p>
    <button type="submit">Login</button>
    </form>
    '''
    return page


app.run(port=8080, host='0.0.0.0')