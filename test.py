from qrcode import qrcode_text_link
from qrcode import qrcode_text_png
from qrcode import qrcode_link_link
from qrcode import qrcode_link_png

print(qrcode_text_link('abc'))
qrcode_text_png('abc')
print(qrcode_link_link('www.baidu.com'))
qrcode_link_png('www.baidu.com')