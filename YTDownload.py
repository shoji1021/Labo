import yt_dlp
import os
import pyfiglet
from colorama import Fore

text = pyfiglet.figlet_format("YouTube Downloader", font="slant")
print(Fore.RED + text)
DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads")

URL = input(Fore.WHITE + "YouTube動画のURLを入力してください: ").strip()

ydl_opts = {
    'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s')
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL])
    print(f"ダウンロードが完了しました！保存先: {DOWNLOAD_DIR}")
