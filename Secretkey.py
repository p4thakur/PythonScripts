#from os import   listdir# we use rom wheni want to ipmort a part let say fun from my class
import os

def rename_file():
	# get the file names from a folder
	file_list=os.listdir(r"C:\Users\Prateek thakur\Desktop\FULL_STACK_DEVELOPER\PYTHON_FOUNDATION\prank\prank")
	print(file_list)
	# now i need to check if i am in riht dire if not change it
	saved_path=os.getcwd()
	print("current working dir is " + saved_path)
	#change the current dir this is because while renaming system look directry where file is
	os.chdir(r"C:\Users\Prateek thakur\Desktop\FULL_STACK_DEVELOPER\PYTHON_FOUNDATION\prank\prank")
	for file_name in file_list:
		#os.rename(file_name, file_name.translate(None,"0123456789")) in oython 2.7 this traslation function will work not here
		table = str.maketrans(dict.fromkeys('0123456789'))
		os.rename(file_name, file_name.translate(table))# rename function use to rename file name, and translate function use to traslate  my fille name and filter out the number in it

#at end change the current work directory else i may face the issue, in this problem my cu
rename_file()
