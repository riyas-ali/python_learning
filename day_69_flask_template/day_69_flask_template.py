from flask import Flask, redirect

app = Flask(__name__, static_url_path="/static")


@app.route("/")
def index():
    return redirect("/portfolio")


@app.route("/portfolio")
def portfolio():
    my_name = 'Kaptain Kitty'
    f = open("template/portfolio.html", "r")
    page = f.read()
    page = page.replace("{name}", my_name)
    f.close()
    return page


app.run(host='0.0.0.0', port=8080)
