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
		compiled_regexes = [re.compile(type) for type in file_types]	
		bools_of_search = [compiled_regex.search(filename) for compiled_regex in compiled_regexes]
		return any(bools_of_search)

	def includes_string(self, open_file, searchstring):
		return searchstring in open_file.read()

#not tested by unit tests!
	def find_matching_filenames(self):
		f = []
		for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
			full_path_names = [os.path.join(dirpath,name) for name in filenames 
						if self.filename_matches_regexes_in_logfind(name)]
			f.extend(full_path_names)

		return f
	
	def open_existing_file_or_die(self, pathname):
		try:
			return open(pathname, 'r')
		except IOError:
			return None

	def find_matched_files_OR_SEARCH(self, matching_file_names):
		matched_files = set()
		for stng in self.searchstring:
			for match_file in matching_file_names:
				x = self.open_existing_file_or_die(match_file)
				if x:
					if self.includes_string(x, stng):
						matched_files.add(x.name)
					x.close()

		return list(matched_files)
