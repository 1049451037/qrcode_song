import qrcode_song as qs

url1 = qs.get_pngurl_by_text('hello world', black = True)
print(url1)
img1 = qs.get_png_by_url(url1)
qs.save_png(img1, './hello.png')

url2 = qs.get_pngurl_by_url('http://www.baidu.com')
print(url2)
img2 = qs.get_png_by_url(url2)
qs.save_png(img2, './baidu.png')