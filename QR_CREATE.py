import qrcode
import pyfiglet
from colorama import Fore

font = pyfiglet.figlet_format("QR Creator")
print(Fore.BLUE+font)
url = input(Fore.WHITE+"リンクを入力してください:")
qr = qrcode.make(url)
qr.show()