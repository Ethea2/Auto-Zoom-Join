import tkinter
from tkinter import *
from auto import openZoom
import datetime


def start():
	start.target_hour = int(time_entry.get()[0:2])
	start.target_minutes = int(time_entry.get()[3:])
	countdownFunction()


def countdownFunction():
	now = datetime.datetime.now()
	target_time = now.replace(hour=start.target_hour, minute=start.target_minutes, second=0, microsecond=0)
	timer = target_time-now
	hours = timer.seconds//3600
	minutes = (timer.seconds//60)%60
	seconds = timer.seconds%60
	if target_time > now:
		countdown.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
		countdown.after(1000,countdownFunction)
	else:
		countdown.config(text="Joining Zoom Meeting...")
		openZoom(f"""{zoom_link.get()}""")


window = tkinter.Tk()
window.geometry("400x200")

#Zoom link entry and label
name_zoom_link = StringVar()
name_zoom_link.set("Zoom Link:")
zoom_link_label = Label(window, textvariable=name_zoom_link, height=2, width=25)
zoom_link_label.grid(row=0, column=0)

zoom_link = Entry(window)
zoom_link.grid(row=0, column=1)

#Time entry and label
time_label_string = StringVar()
time_label_string.set("Time (in military units ex. 13:40): ")
time_label = Label(window, textvariable=time_label_string, height=2, width=25)
time_label.grid(row=1, column=0)

time_entry = Entry(window)
time_entry.grid(row=1, column=1)

#Countdown labels
countdown_label_string = StringVar()
countdown_label_string.set("Countdown: ")
countdown_label = Label(window, textvariable=countdown_label_string, height=4, width=11, font=(30))
countdown_label.grid(row=2, column=0)

countdown = Label(window, text="", font=(30), height=4, width=26)
countdown.grid(row=2, column=1)

start_button = Button(window, text="Start", width=10, command=start)
start_button.grid(row=3, column=1)




window.mainloop()