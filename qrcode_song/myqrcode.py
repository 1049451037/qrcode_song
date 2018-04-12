import requests
from bs4 import BeautifulSoup


def text_link(text, mode=0):
    if text == '':
        return None
    param = {'text': text}
    if mode != 0:
        param['mhid'] = 'thGTD1zpnZohMHcuI9BUPqo'
    url = 'https://cli.im/api/qrcode/code'
    r = requests.get(url, params=param)
    soup = BeautifulSoup(r.text, 'html.parser')
    img = soup.img
    return 'https:' + img['src']


def text_png(text, mode=0, filepath='./', filename='qrcode_song.png'):
    if text == '':
        return None
    link = text_link(text, mode=mode)
    r = requests.get(link)
    with open(filepath + filename, 'wb') as f:
        f.write(r.content)
    return r.content


def link_link(link, mode=0):
    return text_link('//' + link, mode=mode)


def link_png(link, mode=0, filepath='./', filename='qrcode2_song.png'):
    if link == '':
        return None
    _link = link_link(link, mode=mode)
    r = requests.get(_link)
    with open(filepath + filename, 'wb') as f:
        f.write(r.content)
    return r.content
