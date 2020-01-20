import requests
from bs4 import BeautifulSoup
import csv
import re
# pip install beautifulsoup4
# pip install lxml

def get_html(url):
    r = requests.get(url)    # Получим метод Response
    r.encoding = 'utf8'
    return r.text   # Вернем данные объекта text


def csv_read(data):
    with open("data.txt", 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['head'], data['link']))

def get_link(html):
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find('div', id='k2Container').find_all(class_="catItemTitle")
    for i in head:
        link = 'https://ksu.edu.ru/travel' + i.contents[1].get('href')
        heads = i.text
        data = {'head': heads,
                 'link': link}
        csv_read(data)


data = get_link(get_html('https://ksu.edu.ru/travel'))
#https://ksu.edu.ru/travel