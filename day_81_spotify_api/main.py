import os
import requests

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(client_id, client_secret)

response = requests.post(url, data=data, auth=auth)

access_token = response.json()['access_token']

artist = input('Artist: ').lower()
artist = artist.replace(' ', '%20')

url = 'https://api.spotify.com/v1/search'
search = f'?q=artist%3A{artist}&type=track&limit=5'
headers = {'Authorization': f'Bearer {access_token}'}

full_url = f'{url}{search}'
response = requests.get(full_url, headers=headers)
data = response.json()

for track in data['tracks']['items']:
    print(track['name'])
    print(track['album']['external_urls']['spotify'])
