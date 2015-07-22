import os
import sys
import re

class Recurse(object):
	def __init__(self, regex):
		self.regex = regex

	def take_file_return_list(self, open_file):
			
		list_of_regexes = open_file.readlines()
		list_of_regexes = [string.strip() for string in list_of_regexes]
		#figure out how to merge these two
		list_of_regexes = filter(None, list_of_regexes) 	
		
		return list_of_regexes

	def is_log_file(self, filename):
		p = re.compile('\.log')
		return p.search(filename)

	def includes_string(self, open_file, regex):
		if regex in open_file.read():
			return True
		else:
			return False

	def find_matching_filenames(self):
		f = []

		for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
			full_path_names = [os.path.join(dirpath,name) for name in filenames if self.is_log_file(name)]
			f.extend(full_path_names)

		return f
	
	def open_existing_file_or_die(self, pathname):
		
		try:
			return open(pathname, 'r')
		except IOError:
			print 'sorry'
	def find_matched_files(self, matching_file_names):
		list_of_open_files = map(self.open_existing_file_or_die, matching_file_names)
		
		print list_of_open_files
		list_of_open_files  = filter(None, list_of_open_files) 	
		
		print list_of_open_files
		matched_files = [pathname for pathname in list_of_open_files if self.includes_string(pathname, self.regex)]

		return matched_files
