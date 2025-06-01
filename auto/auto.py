import pyautogui
import time
import webbrowser

url = input("Enter the URL of the website:")
webbrowser.open_new_tab(url)

time.sleep(2)

x, y = 1230, 200
pyautogui.click(x, y)
print("Clicked")