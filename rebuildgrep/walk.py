import os
import sys
import re
# regex = raw_input("")

class Recurse(object):
	def __init__(self, regex):
		self.regex = regex

	#open the .logfind file if it exists
	def take_file_return_list(self, fullpath):
		try:
			
			fileobject = open(fullpath, 'r')
			print fullpath
			list_of_regexes = fileobject.read().splitlines()
			list_of_regexes = [string.strip() in list_of_regexes]
			#figure out how to merge these two
			list_of_regexes = filter(None, list_of_regexes) 	
		except:
			list_of_regexes = []
		
		return list_of_regexes

	def is_log_file(self, filename):
		#if the filename contains anything in the /.logfind file, 
		#return True
		p = re.compile('\.log')
		return p.search(filename)

	def includes_string(self, pathname, regex):
		#get this out of here, or just pass the open file into this method so it's easier to 
		#unit test, and that it isn't answering two questions at once
		try:
			reading_file = open(pathname, 'r')
		except IOError:
			return False

		if '/Users/madelynfreed/Library/Containers/com.apple.soagent/Data/Library/Preferences/' in pathname:
			return False
		elif regex in reading_file.read():
			return True
		else:
			return False
		# except:
		# 	print "!!!!!"
		# 	print pathname
		# 	return False
		# else:
		# 	return False

			

	def find_matching_filenames(self):
		f = []

		for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
			full_path_names = [os.path.join(dirpath,name) for name in filenames if self.is_log_file(name)]
			f.extend(full_path_names)

		return f
	def find_matched_files(self, matching_file_names):
		matched_files = [pathname for pathname in matching_file_names if self.includes_string(pathname, self.regex)]

		return matched_files

# test = Recurse()
# f = test.find_matching_filenames()
# matched = test.find_matched_files(f)
# print matched
