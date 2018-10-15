import webbrowser  # we are importing entire webbrowser module
import time
#open up the link in a browser

break_time=3
current_time=0

while (break_time >= 0):
	  print("statring our ",current_time,"iteration")
	  time.sleep(10) 
	  webbrowser.open("https://www.youtube.com/watch?v=mWRsgZuwf_8")
	  break_time=break_time -1 
	  current_time=current_time +1
