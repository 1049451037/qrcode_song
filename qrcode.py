import requests
from bs4 import BeautifulSoup


def qrcode_text_link(text):
    if text=='':
        return None
    param = {'text':text}
    url = 'https://cli.im/api/qrcode/code'
    r = requests.get(url,params=param)
    soup = BeautifulSoup(r.text,'html.parser')
    img = soup.img
    link = img['src']
    return 'https://'+link[2:]

def qrcode_text_png(text , filepath='./' , filename='qrcode_song.png'):
    if text=='':
        return None
    link = qrcode_text_link(text)
    r = requests.get(link)
    with open(filepath+filename,'wb') as f:
        f.write(r.content)

def qrcode_link_link(link):
    return qrcode_text_link('//'+link)

def qrcode_link_png(link , filepath='./' , filename='qrcode2_song.png'):
    if link=='':
        return None
    _link = qrcode_link_link(link)
    r = requests.get(_link)
    with open(filepath+filename,'wb') as f:
        f.write(r.content)