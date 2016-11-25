# qrcode_song
自己做的一个小工具，基于Python3.5,requests,beautifulsoup(bs4),草料二维码API的二维码生成器。<br>

##样例（在test.py中也有）：<br>
```Python
import myqrcode

print(myqrcode.text_link(text='你好'))  # 文本二维码图片的链接
myqrcode.text_png(text='你好', mode=1 ,filepath='./',filename='test1.png')  # 二维码图片保存到本地，mode调整美化模式
print(myqrcode.link_link(link='www.baidu.com')) # 网址的二维码图片的链接
myqrcode.link_png(link='www.baidu.com',filepath='./',filename='test2.png') #实际上函数还会返回图片的二进制存储

```

<br>注：以上功能需要在联网的条件下实现。（因为基于网页爬虫）
