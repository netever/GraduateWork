import requests

def get(url):
    r = requests.get(url)
    r.encoding = 'utf8'
    return r.text