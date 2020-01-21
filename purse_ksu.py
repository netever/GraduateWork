from bs4 import BeautifulSoup

def get_link(html):
    soup = BeautifulSoup(html, 'lxml')
    source = soup.find('div', id='k2Container').find_all(class_="catItemTitle")
    alldata = list()
    for i in source:
        link = 'https://ksu.edu.ru/travel' + i.contents[1].get('href')
        head = i.text
        data = {'head': head,
                 'link': link}
        alldata.append(data)
    return alldata