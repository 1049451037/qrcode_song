import requests
from bs4 import BeautifulSoup

def get_pngurl_by_text(text, black = False):
    if text == '':
        return None
    param = {'text': text}
    if not black:
        param['mhid'] = 'thGTD1zpnZohMHcuI9BUPqo'
    url = 'https://cli.im/api/qrcode/code'
    r = requests.get(url, params = param)
    soup = BeautifulSoup(r.text, 'html.parser')
    img = soup.img
    return 'https:' + img['src']

def get_pngurl_by_url(url, black = False):
    if url.startswith('http://'):
        url = url[7:]
    elif url.startswith('https://'):
        url = url[8:]
    return get_pngurl_by_text('//' + url, black = black)

def get_png_by_url(url):
    r = requests.get(url)
    return r.content

def get_text_png_by_text(text, black = False):
    if text == '':
        return None
    link = get_pngurl_by_text(text, black = black)
    return get_png_by_url(link)

def get_url_png_by_url(url, black = False):
    link = get_pngurl_by_url(url, black = black)
    return get_png_by_url(link)

def save_png(img, fn):
    with open(fn, 'wb') as f:
        f.write(img)
