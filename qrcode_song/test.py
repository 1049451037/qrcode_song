import myqrcode

print(myqrcode.text_link(text='你好'))  # 文本二维码图片的链接
myqrcode.text_png(text='你好', mode=1 ,filepath='./',filename='test1.png')  # 二维码图片保存到本地，mode调整美化模式
print(myqrcode.link_link(link='www.baidu.com')) # 网址的二维码图片的链接
myqrcode.link_png(link='www.baidu.com',filepath='./',filename='test2.png') #实际上函数还会返回图片的二进制存储
