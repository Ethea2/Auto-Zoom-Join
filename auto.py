import pyautogui
import webbrowser
import time
import os


def openZoom(zoom_link):
	print("I am opening browser")
	os.system(f"""python -m webbrowser -t "{zoom_link}""")
	
	enterMeeting()


#recursive function calling itself every task acomplished or error raised.
def enterMeeting():
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
		print("Program finished.")

	elif pyautogui.locateOnScreen('./images/waitingroom.PNG'):
		print("waiting for the host to let you in, trying again in 5 seconds")
		time.sleep(5)
		enterMeeting()

	else:
		enterMeeting()
		print(f"Could not locate anything, trying again in 5 seconds.")
		time.sleep(5)
