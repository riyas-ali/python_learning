import os
import requests
import openai
from dotenv import load_dotenv

load_dotenv()

news_api_key = os.getenv('NEWS_API')
openai_api_key = os.getenv('OPENAI_API_KEY')
organisation_id = os.getenv('OPENAI_ORG_ID')

openai.organization = organisation_id
openai.api_key = openai_api_key
openai.Model.list()

country = 'us'
url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_api_key}'

result = requests.get(url)
data = result.json()


def summarise(text):
    response = openai.Completion.create(model='text-davinci-003',
                                        prompt=text,
                                        temperature=0,
                                        max_tokens=20)
    print(response['choices'][0]['text'].strip())


counter = 0
for article in data['articles']:
    counter += 1
    if counter > 5:
        break
    prompt = f"Summarise {article['url']} in one sentence."
    summarise(prompt)
