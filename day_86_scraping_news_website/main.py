import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

my_links = soup.find_all("span", {'class': 'titleline'})

interests = ['apple', 'angular', 'python', 'javascript', 'google', 'microsoft']

for link in my_links:
    text = link.text
    text_list = text.split()
    contains_word = False
    for word in text_list:
        if word.lower() in interests:
            contains_word = True
    if contains_word:
        print(link.text)
        my_link = link.find_all("a")
        print(my_link[0]['href'])
