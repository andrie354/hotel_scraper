import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.pegipegi.com/hotel/bogor/3.html'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
details = soup.find_all('div', {'class': 'listContent'})
for detail in details:
    try:
        name = detail.find('div', {'class': 'title'})\
            .text.replace('\n','').strip()
        location = detail.find('div', {'class': 'address'})\
            .text.replace('\n','').replace('    Tampilkan Peta','').strip()
        price = detail.find('div', {'class': 'diskonPrice'})\
            .text.replace('\n','').strip()
    except:
        name = 'none'
        location = 'none'
        price = 'none'

    hotel_info = {
        'name': name,
        'location': location,
        'price': price
    }

    time.sleep(3)
    print(hotel_info)

