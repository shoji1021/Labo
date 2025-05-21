import qrcode
url = input()
qr = qrcode.make(url)
qr.show()