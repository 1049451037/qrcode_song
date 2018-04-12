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

# Sample(test.py)
```Python
import myqrcode

print(myqrcode.text_link(text='你好'))  # 文本二维码图片的链接
myqrcode.text_png(text='你好', mode=1 ,filepath='./',filename='test1.png')  # 二维码图片保存到本地，mode调整美化模式
print(myqrcode.link_link(link='www.baidu.com')) # 网址的二维码图片的链接（这里不要加http://或者https://）
myqrcode.link_png(link='www.baidu.com',filepath='./',filename='test2.png') # 实际上函数还会返回图片的二进制存储
```

# Goal
1. Usage
```Python
import qrcode_song as qs

url = qs.geturl('hello')
image = qs.getimage(url)
qs.save(image)
```
2. Install
```
pip install qrcode_song
```