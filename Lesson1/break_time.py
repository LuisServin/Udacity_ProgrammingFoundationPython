# !usr/bin/env python

# import the library to use the web browser
import webbrowser
# library for time functions
import time

total_break = 1
break_count = 0

print "This program started on " + time.ctime()
while(break_count < total_break):
	# wait 10 seconds 
	time.sleep(2 * 60 * 60)
	# open the web browser
	webbrowser.open("https://www.youtube.com/watch?v=pUjE9H8QlA4")
	break_count = break_count + 1