import webbrowser

left = "https://music.youtube.com/watch?v="
right = "&list=RDAMVM"
ID = input("Enter the ID of the song:")
url = left + ID + right

webbrowser.open_new_tab(url)