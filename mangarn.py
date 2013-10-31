#!/usr/bin/python

import os
import string
import sys
import getopt
import re

class bcolors:
	YELLOW = '\033[93m'
	ENDC = '\033[0m'

	def disable(self):
		self.YELLOW =''
		self.ENDC = ''

#default settings
appname = 'mangarn'
version = '0.1'
img_ext = ['jpg','jpeg','png']

show_infomation = True #contorls if the program 
			#show infomation to stdout
level = 3              #example level = 3 then 1.jpg => 001.jpg

prefix=''		#prefix added to the changed filename

def usage():
	print 'usage:%s [-hsl] [arg]'%appname

def change_name(file):
	if os.path.isfile(file):
		#deal with file name
		file_list = file.split('.')
		file_list_len = len(file_list)
		file_ext = file_list[file_list_len -1]
		file_name = '.'.join(file_list[0:file_list_len-1])

		#search digit in file_name
		p = re.compile(r"[0-9]+")
		m = p.search(file_name)
		if m:
			i = string.atoi(m.group())
		else:
			#no match
			return

		#deal with the picture
		if file_ext in img_ext:
			new_file_name = ('%%0%dd'%level)%i
			newfile = prefix + new_file_name +'.'+ file_ext
			if show_infomation:
				print 	bcolors.YELLOW +\
					'{0: >10}'.format(file) +\
					' => '+\
					'{0: >10}'.format(newfile)+\
					bcolors.ENDC
			os.rename(file,newfile)


			
def main(argv):
	#deal with opts
	try:
		opts,args =\
		getopt.getopt(argv,'hsl:p:',\
		['help','silent','level=','prefix='])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt,arg in opts:
		if opt in ("-h","--help"):
			usage()
			sys.exit()
		elif opt in ('-s','--silent'):
			global show_infomation
			show_infomation = False
		elif opt in ('-l','--level'):
			global level
			# to see if the arg is only a number
			p = re.compile(r"[0-9]+")
			m = p.match(arg)
			if m:
				level = string.atoi(arg)
			else:
				print '%s:wrong argument'%appname 
				sys.exit(2)
		elif opt in ('-p','--prefix'):
			global prefix
			prefix = arg
	
	dir = os.getcwd()
	files = os.listdir(dir)
	for file in files:
		change_name(file)

if __name__ == "__main__":
	main(sys.argv[1:])
