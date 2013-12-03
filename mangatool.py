#!/usr/bin/env python

import sys
import getopt
import re
import os
import string
class bcolors:
	YELLOW = '\033[93m'
	RED    = '\033[91m'
	ENDC = '\033[0m'
class MangaToolSettings(object):
	def __init__(self):
		self.reset()
	def reset(self):
		self.level = 2
		self.img_ext = {'jpg','jpeg','png'}
		self.show_infomation = True
		self.do_nothing = False
		self.prefix=''
	

class MangaTool(object):
	# app infomations 
	app_name = 'MangaTool'
	major_version = 0
	minor_version = 2
	micro_version = 0
	version = '0.2.0'
	usage_infomation = ''
	@classmethod
	def print_app_infomation(cls):
		print '%s:version:%s'%(cls.app_name,cls.version)
	
	@classmethod 
	def print_usage(cls):
		print 'Usage:'+cls.usage_infomation

	def __init__(self):
		self.settings = MangaToolSettings()
	
	def __change_file(self,file):
		if os.path.isfile(file):
			#dealwith filename
			filename,ext = os.path.splitext(file)
			# search digit in filename
			p = re.compile(r"[0-9]+")
			m = p.search(filename)
			if m:
				i = string.atoi(m.group())
			else:
				#no match
				return
			#change file name now
			if (ext[1:] in self.settings.img_ext):
				new_filename = \
				('%%0%dd'%self.settings.level)%i
				newfile = self.settings.prefix+\
						new_filename +\
						ext
				if self.settings.show_infomation:
					print bcolors.YELLOW +\
					      '{0: >10}'.format(file) +\
					      ' => ' +\
					      '{0: >10}'.format(newfile) +\
					      bcolors.ENDC
				if not self.settings.do_nothing:
					os.rename(file,newfile)

	def rename(self,files):
		for file in files:
			self.__change_file(file)



def main(argv):
	if len(argv) == 0:
		MangaTool.print_usage()
		return -1

	command = argv[0]
	try:
		opts,args = \
			getopt.getopt(argv[1:],'sl:e:p:n',\
			['silent','level=','ext=','prefix=','donothing'])
	except getopt.GetoptError:
		MangaTool.print_usage()
		sys.exit(2)


	if command == 'rename':
		#rename function
		mt = MangaTool()
		#get settings
		for opt,arg in opts:
			if opt in ('-s','silent'):
				mt.settins.show_infomation = False
			elif opt in ('-l','--level'):
				#to see if the arg is a number
				p = re.compile(r"[0-9]+")
				m = p.match(arg)
				if m:
					mt.settings.level = string.atoi(arg)
				else:
					print '%s %s :wrong argument %s'%\
							(mt.app_name,\
							 command,
							 arg)
					sys.exit(-1)
			elif opt in ('-e','--ext'):
				mt.settings.img_ext = arg.split(',')
			elif opt in ('-p','--prefix'):
				mt.settings.prefix = arg
			elif opt in ('-n','--donothing'):
				mt.settings.do_nothing = True
		#now get target dir
		if len(args) == 0:
			dirs = [os.getcwd()]
		else:
			dirs = args
		for dir in dirs:
			if os.path.isdir(dir):
				os.chdir(dir)
				print 'Dir:%s'%dir
				files = os.listdir(dir)
				mt.rename(files)
			else:
				print '%sError:%s %s not a dir'%\
					(bcolors.RED,bcolors.ENDC,dir)
				
		
	elif command == 'help':
		MangaTool.print_usage()
	else:
		print '%sError:%s unknown command :%s'\
				%(bcolors.RED,bcolors.ENDC,command)
	

if __name__ == '__main__':
	main(sys.argv[1:])

