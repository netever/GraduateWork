import requests
from bs4 import BeautifulSoup

def get(url):
    r = requests.get(url)  # Получим метод Response
    r.encoding = 'utf8'
    return r.text  # Вернем данные объекта text