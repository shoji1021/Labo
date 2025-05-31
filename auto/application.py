import pyautogui
import time

time.sleep(3)  # 準備時間

button = pyautogui.locateCenterOnScreen('button.png', confidence=0.8)  # 画面上で画像を探す
if button:
    pyautogui.click(button)  # ボタンをクリック
    print("ボタンをクリックしました！")
else:
    print("ボタンが見つかりませんでした。")
