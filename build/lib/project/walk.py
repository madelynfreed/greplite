import os
from sys import argv
print argv
script, regex = argv

# regex = raw_input("")

class Recurse(object):
	def is_log_file(self, filename):
		if "." in filename:
			return True
		else:
			return False

	def includes_string(self, pathname, regex):
		reading_file = open(pathname, 'r')

		if regex in reading_file.read():
			return True
		else:
			return False

	def find_matching_filenames(self):
		f = []

		for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
			full_path_names = [os.path.join(dirpath,name) for name in filenames if self.is_log_file(name)]
			f.extend(full_path_names)

		return f
	def find_matched_files(self, matching_file_names):
		matched_files = [pathname for pathname in matching_file_names if self.includes_string(pathname, regex)]

		return matched_files

# test = Recurse()
# f = test.find_matching_filenames()
# matched = test.find_matched_files(f)
# print matched
