import requests
from bs4 import BeautifulSoup

url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

my_links = soup.findAll('a', {'class': 'css-19v1rkv'})
counter = 0
for link in my_links:
    if counter > 1:
        print(link.text)
        print(f"https://www.yelp.com{link['href']}")
    counter += 1
