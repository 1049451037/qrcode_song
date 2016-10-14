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
