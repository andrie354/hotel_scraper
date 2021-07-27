import requests
from bs4 import BeautifulSoup


url = 'https://www.pegipegi.com/hotel/bogor/1.html'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
details = soup.find_all('div', {'class': 'contentLeft'})
for detail in details:
    name = detail.find('div', {'class': 'title'}).text
    rating = detail.find('div', {'class': 'ratingRight'}).find_all('span')[0].text
    print(rating)

