import pyautogui
import webbrowser
import os

location = os.path.realpath(
			os.path.join(os.getcwd(), os.path.dirname(__file__)))
img_folder = os.path.join(location, "images")

waitPNG = f"{img_folder}\\wait.PNG"

def openZoom(zoom_link):
	webbrowser.open(zoom_link)
	print(os.listdir(img_folder))


# pyautogui.click(x=1916,y=1050, button="left")

# pyautogui.press("win")
# pyautogui.write("zoom")
# pyautogui.press("enter")