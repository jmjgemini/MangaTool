#!/usr/bin/python

import os
import string

def change_name(file,level):
	if os.path.isfile(file):
		lists = file.split('.')
		file_name= lists[0]
		file_ext = lists[1]
		if file_ext in img_ext:
			i = string.atoi(file_name)
			new_file_name = '%03d'%i
			newfile = new_file_name +'.'+ file_ext
			print 'changeing '+file+' to '+ newfile
			os.rename(file,newfile)


			
		
img_ext = ['jpg','jpeg','png']
dir = os.getcwd()
files = os.listdir(dir)
level = 3

for file in files:
	change_name(file,level)


