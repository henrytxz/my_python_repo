import time
import webbrowser

minute=60
hour=60*60
interval = 25*minute
total_breaks = 8*hour/(30*minute)
break_count = 0
print ("This program started on: " + time.ctime())
while break_count < total_breaks:
	time.sleep(interval)
	webbrowser.open("https://www.youtube.com/watch?v=b2njHW9ydWs")
	break_count += 1

