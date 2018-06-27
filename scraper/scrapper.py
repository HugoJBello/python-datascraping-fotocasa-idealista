import requests
from bs4 import BeautifulSoup

class Scrapper:

    def __init__(self, urls):
        self.urls = urls
    
    def get_data(self):
        for url in self.urls:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
            page = requests.get(url,headers=headers)
            print(page.text)
            soup = BeautifulSoup(page.text, 'html.parser')
            properties = soup.find(class_='item-info-container')
            for prop in properties:
                print(prop.prettify())

            prizes = properties.find(class_='item-price h2-simulated')
            for prop in prizes:
                print(prop.prettify())


