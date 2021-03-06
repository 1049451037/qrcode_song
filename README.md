# qrcode_song

A qrcode generator(crawler) based on [cli-qrcode](https://cli.im/) and web spider. Read documents [here](https://1049451037.github.io/qrcode_song/).

# Requirements

* Python 3
* requests
* beautifulsoup(bs4)
* Internet

# Functions

Main function:

* Generate(crawler) a qrcode image and return the URL of that qrcode image.

Auxiliary functions:

* Get binary qrcode image content by URL.
* Save qrcode image to disk.

# Installation

```shell
pip install qrcode-song
```
    
# Test

```python
>>> import qrcode_song as qs
>>> qs.get_pngurl_by_text('wow')
'https://qr.api.cli.im/qr?...e6eb'
```

# Tutorial

Actually, you will know all functions of this project in test.py.

```python
import qrcode_song as qs

url1 = qs.get_pngurl_by_text('hello world', black = True)
# print url1 or print(url1)
img1 = qs.get_png_by_url(url1)
qs.save_png(img1, './hello.png')

url2 = qs.get_pngurl_by_url('http://www.baidu.com') # this function also has 'black' parameter
# print url2 or print(url2)
img2 = qs.get_png_by_url(url2)
qs.save_png(img2, './baidu.png')
```
