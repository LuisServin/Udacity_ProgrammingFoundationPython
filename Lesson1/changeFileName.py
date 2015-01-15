# !usr/bin/env python

# Program to get all the files from a directory a rename then
# eliminating the number :D

# library to get access to files
import os

def rename_files():
	# (1) get file names from a folder
	file_list = os.listdir(r"/home/luis/Documents/Tutoriales/Python/PythonProgCourse/Lesson1/prank/prank")
	# print file_list
	saved_path = os.getcwd()
	print "Current working directory is " + saved_path

	# change the working directory 
	os.chdir("/home/luis/Documents/Tutoriales/Python/PythonProgCourse/Lesson1/prank/prank")
	# (2) for each file, rename file
	for file_name in file_list:
		# rename the files
		print "Old file name - " + file_name
		print "New file name - " + file_name.translate(None,"1234567890")
		os.rename(file_name,file_name.translate(None,"1234567890"))
	os.chdir(saved_path)

# call the function
rename_files()