import os
import sys
import re

class Greplite(object):
	def __init__(self, searchstring, configfile):
		self.searchstring = searchstring
		#self.logfindfile = os.path.join(os.path.expanduser('~'), '.logfind')
		self.configfile = configfile
#rename to be more of a noun?
	def filename_patterns_from_file(self):
		open_file = self.open_existing_file_or_die(self.configfile)
		filename_patterns = open_file.readlines()
		filename_patterns = [string.strip() for string in filename_patterns]
		#figure out how to merge these two
		filename_patterns = filter(None, filename_patterns) 	
		
		return filename_patterns

	def filename_matches_regexes_in_logfind(self, filename):
		file_types = self.filename_patterns_from_file()
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
	
	def find_matched_files_AND_SEARCH(self, matching_file_names):
		matched_files = []
		for fle in matching_file_names:
			boolist = [] 
			for search_string in self.searchstring: 
				x = self.open_existing_file_or_die(fle)
				boolist.append(self.includes_string(x, search_string))
				x.close()
			if all(boolist):
				matched_files.append(fle)
		return matched_files
