import pyqrcode,png
url = pyqrcode.create('http://uca.edu')
url.png('qr.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
url.show()