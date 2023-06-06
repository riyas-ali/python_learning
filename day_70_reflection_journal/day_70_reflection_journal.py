from flask import Flask

app = Flask(__name__)

my_reflections = {"78": {"link": "https://replit.com/@RiyasAli/Day78100Days#template/reflection.html",
                         "Reflection": "was a bit of a head scratcher, but I got there in the end. Even if I was a bit "
                                       "lazy with the css"},
                  "79": {"link": "https://replit.com/@RiyasAli/Day78100Days#template/reflection.html",
                         "Reflection": "Oh. Easy. Done. Boom"}}


@app.route('/<page_number>')
def index(page_number):
    page = ''
    f = open("template/reflection.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{day}", page_number)
    page = page.replace("{link}", my_reflections[page_number]["link"])
    page = page.replace("{reflection}", my_reflections[page_number]["Reflection"])
    return page


app.run(host='0.0.0.0', port=8080)
