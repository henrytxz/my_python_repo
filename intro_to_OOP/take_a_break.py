import time
import webbrowser

total_breaks = 8
break_count = 0
print ("This program started on: " + time.ctime())
while break_count < total_breaks:
	time.sleep(3600)
	webbrowser.open("https://www.youtube.com/watch?v=b2njHW9ydWs")
	break_count += 1

