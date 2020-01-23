import web
from bs4 import BeautifulSoup

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    source = soup.find('div', id='k2Container').find_all(class_="catItemTitle")
    alldata = list()
    for i in source:
        link = 'https://ksu.edu.ru' + i.contents[1].get('href')
        head = i.text
        text = __get_text(web.get(link))
        tags = __get_tags(web.get(link))
        data = {'head': head,
                'link': link,
                'text': text,
                'tags': tags,
                'type': "nobody"}
        alldata.append(data)
    return alldata

def __get_text(html):
    soup = BeautifulSoup(html, 'lxml')
    source = soup.find('div', id='k2Container').find_all('p')
    text = ""
    for i in source:
        text = text + i.text
    return text

def __get_tags(html):
    soup = BeautifulSoup(html, 'lxml')
    source = soup.find('div', id='k2Container').find_all('li')
    tags = ""
    for i in source:
        tags = tags + "#" + i.text + " "
    return tags