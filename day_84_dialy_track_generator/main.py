import os
import requests
import openai
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

news_api_key = os.getenv('NEWS_API')
openai_api_key = os.getenv('OPENAI_API_KEY')
organisation_id = os.getenv('OPENAI_ORG_ID')
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

openai.organization = organisation_id
openai.api_key = openai_api_key
openai.Model.list()

country = 'us'
url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_api_key}'

result = requests.get(url)
data = result.json()
responses = []


def summarise(text):
    openai_response = openai.Completion.create(model='text-davinci-003',
                                               prompt=text,
                                               temperature=0,
                                               max_tokens=4)
    for item in openai_response['choices']:
        responses.append(item['text'].strip())


counter = 0
for article in data['articles']:
    counter += 1
    if counter > 5:
        break
    prompt = f"Summarise {article['url']} in no more than four words."
    summarise(prompt)

url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(client_id, client_secret)

response = requests.post(url, data=data, auth=auth)

access_token = response.json()['access_token']

for response in responses:
    print(response)
    headline = response.replace(' ', '%20').replace('.', '')
    url = 'https://api.spotify.com/v1/search'
    search = f'?q={headline}&type=track&limit=1'
    headers = {'Authorization': f'Bearer {access_token}'}
    full_url = f'{url}{search}'
    response = requests.get(full_url, headers=headers)
    data = response.json()
    for track in data['tracks']['items']:
        print(track['album']['external_urls']['spotify'])
