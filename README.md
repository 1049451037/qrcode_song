# qrcode_song
自己做的一个小工具，基于Python3.5,requests,beautifulsoup(bs4),草料二维码API的二维码生成器。<br>

## 主要功能：
1.生成（爬取）文本的二维码图片并保存到本地；<br>
2.获取文本的二维码图片的链接；<br>
3.生成（爬取）网址的二维码图片并保存到本地；<br>
4.获取网址的二维码图片的链接。<br>

## 样例（在test.py中也有）：<br>
```Python
import myqrcode

print(myqrcode.text_link(text='你好'))  # 文本二维码图片的链接
myqrcode.text_png(text='你好', mode=1 ,filepath='./',filename='test1.png')  # 二维码图片保存到本地，mode调整美化模式
print(myqrcode.link_link(link='www.baidu.com')) # 网址的二维码图片的链接（这里不要加http://或者https://）
myqrcode.link_png(link='www.baidu.com',filepath='./',filename='test2.png') # 实际上函数还会返回图片的二进制存储

```

<br>
使用时只需要把myqrcode.py文件放到工程的目录下就可以import myqrcode来使用了。
<br>
注：以上功能需要在联网的条件下实现。（因为基于网页爬虫）
