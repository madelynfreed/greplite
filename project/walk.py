import os

def is_log_file(filename):
	return True

f = []
for (dirpath, dirnames, filenames) in os.walk("."):
	full_path_names = [os.path.join(dirpath,name) for name in filenames if is_log_file(name)]
	f.extend(full_path_names)

print f

	