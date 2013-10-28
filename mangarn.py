#!/usr/bin/python

import os
import string

def change_name(file,level):
	if os.path.isfile(file):
		#deal with file name
		file_list = file.split('.')
		file_list_len = len(file_list)
		file_ext = file_list[file_list_len -1]
		file_name = file_list[0:file_list_len-2]


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


