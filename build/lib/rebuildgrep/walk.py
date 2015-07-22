import os
import sys
import re
class Recurse(object):
	def __init__(self, searchstring):
		self.searchstring = searchstring
		self.logfindfile = os.path.join(os.path.expanduser('~'), '.logfind')

	def take_file_return_list(self, open_file):
		list_of_regexes = open_file.readlines()
		list_of_regexes = [string.strip() for string in list_of_regexes]
		#figure out how to merge these two
		list_of_regexes = filter(None, list_of_regexes) 	
		
		return list_of_regexes

	def filename_matches_regexes_in_logfind(self, filename):
		file_types = self.take_file_return_list(self.open_existing_file_or_die(self.logfindfile))
		#compile each of the elements in file_types
		#if each.search(filename) , return true
		compiled_regexes = [re.compile(type) for type in file_types]	
		bools_of_search = [compiled_regex.search(filename) for compiled_regex in compiled_regexes]
		return any(bools_of_search)

	def includes_string(self, open_file, searchstring):
		if searchstring in open_file.read():
			return True
		else:
			return False

	def find_matching_filenames(self):
		f = []

		for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
			full_path_names = [os.path.join(dirpath,name) for name in filenames if self.filename_matches_regexes_in_logfind(name)]
			f.extend(full_path_names)

		return f
	
	def open_existing_file_or_die(self, pathname):
		
		try:
			return open(pathname, 'r')
		except IOError:
			return None

	def find_matched_files(self, matching_file_names):
		list_of_open_files = map(self.open_existing_file_or_die, matching_file_names)
		
		list_of_open_files  = filter(None, list_of_open_files) 	
		
		matched_files = [pathname for pathname in list_of_open_files if self.includes_string(pathname, self.searchstring[0])]
		for open_file in matched_files:
			open_file.close()
		return matched_files
