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


class setting:
	@classmethod
	def reset(cls):
		cls.appname = 'magarn'
		cls.version = '0.12'
		cls.img_ext = ['jpg','jpeg','png']
		cls.show_infomation = True
		cls.level   = 3
		cls.prefix  = ''

		
def usage():
	print 'usage:%s [-hslp] [arg]'%setting.appname

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
		if file_ext in setting.img_ext:
			new_file_name = ('%%0%dd'%setting.level)%i
			newfile = setting.prefix +\
				new_file_name +'.'+ file_ext
			if setting.show_infomation:
				print 	bcolors.YELLOW +\
					'{0: >10}'.format(file) +\
					' => '+\
					'{0: >10}'.format(newfile)+\
					bcolors.ENDC
			os.rename(file,newfile)


			
def main(argv):
	#deal with opts
	setting.reset()
	try:
		opts,args =\
			getopt.getopt(argv,'hsl:e:p:',\
		['help','silent','level=','ext=','prefix='])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt,arg in opts:
		if opt in ("-h","--help"):
			usage()
			sys.exit()
		elif opt in ('-s','--silent'):
			setting.show_infomation = False
		elif opt in ('-l','--level'):
			# to see if the arg is only a number
			p = re.compile(r"[0-9]+")
			m = p.match(arg)
			if m:
				setting.level = string.atoi(arg)
			else:
				print '%s:wrong argument'%setting.appname 
				sys.exit(2)
		elif opt in ('-e','--ext'):
			setting.img_ext = arg.split(',')
		elif opt in ('-p','--prefix'):
			setting.prefix = arg
	
	dir = os.getcwd()
	files = os.listdir(dir)
	for file in files:
		change_name(file)

if __name__ == "__main__":
	main(sys.argv[1:])
