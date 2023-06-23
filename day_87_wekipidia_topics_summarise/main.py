import requests
from bs4 import BeautifulSoup
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
organisation_id = os.getenv('OPENAI_ORG_ID')

openai.organization = organisation_id
openai.api_key = openai_api_key
openai.Model.list()

wiki_url = input("paste wiki url here: ")

url = wiki_url
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

articles = soup.find_all('div', {'class': 'mw-parser-output'})

text = ''
for article in articles:
    content = article.find_all('p')
    for p in content:
        text += p.text

prompt = f'Summarise the text below in no more than 3 paragraphs."{text}"'
ai_response = openai.Completion.create(model='text-davinci-003',
                                       prompt=prompt,
                                       temperature=0,
                                       max_tokens=150)

refs = soup.find_all('ol', {'class': 'references'})

for ref in refs:
    print(ref.text.replace('^ ', ''))

print('Summary: ',ai_response['choices'][0]['text'].strip())

