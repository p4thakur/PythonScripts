# google have a website that actuall check wether i have curse word or not
# we can use it find all the curse word possible
import urllib.request

def read_text():

	quotes=open(r"C:\Users\Prateek thakur\Desktop\FULL_STACK_DEVELOPER\great_mind.txt") #in oython3.0 r need to be added here whic convert it to raw string
	content_of_file=quotes.read()
	print(content_of_file)
	quotes.close()
	#lets call our checker function
	profinatycheck(content_of_file)


def profinatycheck(text):
	#establis the connect with our websote 

	#connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)# this work on python 2.7
	connection=urllib.request.urlopen("http://www.wdy.com/profanity?q=/"+text) # it throwing me error due to this urrl its not valid anymore
	output=connection.read()
	print(output)
	connection.close()


read_text()

#so open is use to read the file from disl
#urllib is used to open connection from a website