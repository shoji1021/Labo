import qrcode
url = input("リンクを入力してください:")
qr = qrcode.make(url)
qr.show()