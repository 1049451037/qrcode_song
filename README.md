# qrcode_song
A qrcode generator(crawler) based on cli-qrcode and web spider.

# Requirement
* Python3.5+
* requests
* beautifulsoup(bs4)
* Internet

# Function
Main function: Generate(crawler) a qrcode image and return the URL of that qrcode image.

Auxiliary functions:
* Get binary qrcode image content by URL.
* Save qrcode image to disk.

# Install
1. Download this repository.
2. Change current directory into this folder.
3. (Optional) Run test code.
    ```
    python test.py
    ```
    You will get two qrcode urls and two images.
4. Installation.
    ```
    pip install .
    ```
5. Test in terminal.
    ```
    >>> import qrcode_song as qs
    >>> qs.get_pngurl_by_text('wow')
    'https://qr.api.cli.im/qr?...e6eb'
    ```

# Tutorial
Actually, you will know all functions of this project in test.py.
```Python
import qrcode_song as qs

url1 = qs.get_pngurl_by_text('hello', black = True)
print(url1)
img1 = qs.get_png_by_url(url1)
qs.save_png(img1, './hello.png')
url2 = qs.get_pngurl_by_url('http://www.baidu.com')
print(url2)
img2 = qs.get_png_by_url(url2)
qs.save_png(img2, './baidu.png')
```
