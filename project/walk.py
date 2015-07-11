import os
from sys import argv

script, regex = argv

def is_log_file(filename):
	return True

def includes_string(pathname, regex):
	reading_file = open(pathname, 'r')

	if regex in reading_file.read():
		return True
	else:
		return False

f = []
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
	full_path_names = [os.path.join(dirpath,name) for name in filenames if is_log_file(name)]
	f.extend(full_path_names)

# print f

matched_files = [pathname for pathname in f if includes_string(pathname, regex)]

print matched_files

	

