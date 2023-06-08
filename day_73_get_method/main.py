from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    get = request.args
    if get["name"].lower() == "riyas":
        return "Hello Boss"
    return "No data"


@app.route('/language')
def lang():
    data = request.args
    if data == {}:
        return "Nothing here"
    if data["lang"] == "eng":
        return "Hello, and welcome to our wonderful website"
    if data["lang"] == "mal":
        return "ഹലോ, ഞങ്ങളുടെ അത്ഭുതകരമായ വെബ്സൈറ്റിലേക്ക് സ്വാഗതം"


app.run(host='0.0.0.0', port=8080)
