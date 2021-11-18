import pyautogui
import webbrowser
import time


def openZoom(zoom_link):
	webbrowser.open_new_tab(zoom_link)
	enterMeeting()

def enterMeeting():
	try:
		time.sleep(3)
		if pyautogui.locateOnScreen('./images/wait.PNG'):
			print("waiting for host to start, checking again in 5 seconds")
			time.sleep(5)
			enterMeeting()
		elif pyautogui.locateOnScreen('./images/launch.PNG'):
			print("Launch button found")
			launchX, launchY = pyautogui.locateCenterOnScreen('./images/launch.PNG')
			pyautogui.click(launchX, launchY)
			time.sleep(4)
			enterMeeting()
		elif pyautogui.locateOnScreen('./images/signin.PNG'):
			print("signin located")
			time.sleep(2)
			signinX, signinY = pyautogui.locateCenterOnScreen('./images/signin.PNG')
			pyautogui.click(signinX, signinY)
			time.sleep(5)
			enterMeeting()
		elif pyautogui.locateOnScreen('./images/join.PNG'):
			print("join located")
			time.sleep(2)	
			launchX, launchY = pyautogui.locateCenterOnScreen('./images/join.PNG')
			pyautogui.click(launchX, launchY)
		elif pyautogui.locateOnScreen('./images/waitingroom.PNG'):
			print("waiting for the host to let you in, trying again in 5 seconds")
			time.sleep(5)
			enterMeeting()

	except:
		enterMeeting()
		print("Could not locate anything, trying again in 5 seconds")
		time.sleep(5)

openZoom("https://zoom.us/j/97248362032?pwd=Q1JmNW12Nkpua3pScUhOa1EwczdOQT09")

# pyautogui.click(x=1916,y=1050, button="left")

# pyautogui.press("win")
# pyautogui.write("zoom")
# pyautogui.press("enter")