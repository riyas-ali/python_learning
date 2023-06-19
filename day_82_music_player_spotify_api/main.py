import json

from flask import Flask, render_template, request
import os, requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(client_id, client_secret)

response = requests.post(url, data=data, auth=auth)

access_token = response.json()['access_token']

year = 1990
offset = 0

headers = {'Authorization': f'Bearer {access_token}'}
url = 'https://api.spotify.com/v1/search'
search = f'?q=year%3A{year}&type=track&limit=10&offset={offset}'

full_url = f'{url}{search}'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', value=year)


@app.route('/', methods=['POST'])
def get_songs():
    global year
    form = request.form
    year = form['year']
    search = f'?q=year%3A{year}&type=track&limit=10&offset={offset}'
    full_url = f'{url}{search}'
    response = requests.get(full_url, headers=headers)
    print(full_url)
    data = response.json()

    music_list = []

    for track in data['tracks']['items']:
        track_name = track['name']
        track_url = track['external_urls']['spotify']
        result = requests.get(track_url, headers=headers)
        music = {'track_name': track_name, 'url': track_url}
        music_list.append(music)
    return render_template('index.html', music_list=music_list, value=year)


app.run(host='0.0.0.0', port=8080)
