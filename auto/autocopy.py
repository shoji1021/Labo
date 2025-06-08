import pyautogui
import time
import webbrowser

url = "https://orteil.dashnet.org/cookieclicker/"
webbrowser.open_new_tab(url)

time.sleep(7)

x = 300
y = 500
start = time.time()

while True:
    pyautogui.click(x, y)
    print("Clicked")
    if time.time() - start > 30:
        print("秒後に終了します")
        break