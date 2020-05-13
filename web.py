import requests

def get(url):
    r = requests.get(url)  # Получим метод Response
    r.encoding = 'utf8'
    return r.text  # Вернем данные объекта text