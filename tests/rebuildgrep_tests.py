from nose.tools import *
from rebuildgrep import walk
import os
import subprocess
import unittest

def build_greplite_object(searchstring, configfile):
	return walk.Greplite(searchstring, configfile)

class TestClass():

	def setup(self):
		file_extensions = ['\.log','\.txt','\.py', 'vegan']	
		self.path = os.path.join(os.path.expanduser('~'), '.logfind')
		self.f = open(self.path, 'w+')
		for string in file_extensions:
			self.f.write(string + '\n')
		self.f.close()

		file_content = """Etsy vegan migas, sustainable letterpress High 
				Life hashtag messenger bag beard. Pug scenester 
				bicycle rights, put a bird on it 3 wolf moon 
				meditation cray Pitchfork craft beer biodiesel."""
		self.text_file_path = os.path.join(os.path.expanduser('~'), 'teester.txt')
		self.textfile = open(self.text_file_path, 'w+')
		self.textfile.write(file_content)
		self.textfile.close()
	def teardown(self):
		os.remove(self.path)
		os.remove(self.text_file_path)
	
	def test_filename_matches_regexes_in_logfind(self):
		x = build_greplite_object('_', self.path)
		assert(x.filename_matches_regexes_in_logfind("gorp.log"))
		
	def test_does_not_match_regex_in_logfind(self):
		x = build_greplite_object('_', self.path)
		assert_false(x.filename_matches_regexes_in_logfind("blgy.p"))

	def test_is_close_but_does_not_match_regex_in_logfind(self):
		x = build_greplite_object('_', self.path)
		assert_false(x.filename_matches_regexes_in_logfind("blog.lo"))

	def test_logfind_file_exists_empty(self):

		path = os.path.join(os.path.expanduser('~'), 'file_that_exists')
		f = open(path, 'w+')
		f.close()
		f = open(path, 'r')
		x = build_greplite_object('_', path)
		assert(x.filename_patterns_from_file() == [])
		f.close()
		os.remove(path)
	def test_logfind_file_exists_with_regexes(self):
		
		x = build_greplite_object('_', self.path)
		self.f = open(self.path, 'r')
		assert_false(x.filename_patterns_from_file() == [])
		self.f.close()
	
	def test_includes_string(self):
		
		x = build_greplite_object('_', self.text_file_path)
		textfile = open(self.text_file_path, 'r')
		assert(x.includes_string(textfile, 'Pitchfork'))
	def test_find_matched_files_false(self):
		x = build_greplite_object(['Pitchfork', 'vegan'], self.path)
		file_name_array = [self.path, self.text_file_path, 'path/that/doesnt/exist']
		assert_false(file_name_array == x.find_matched_files_OR_SEARCH(file_name_array))

	def test_find_matched_files_true(self):
		x = build_greplite_object(['Pitchfork', 'pug'], self.path)
		file_name_array = [self.text_file_path, self.path]
		assert([str(self.text_file_path)] == x.find_matched_files_OR_SEARCH(file_name_array))


	def test_OR_search(self):
		x = build_greplite_object(['Pitchfork', 'vegan'], self.path)
		file_name_array = [self.text_file_path, self.path]
		assert(file_name_array == x.find_matched_files_OR_SEARCH(file_name_array))

	def test_AND_search(self):
		x = build_greplite_object(['Pitchfork', 'vegan'], self.path)
		file_name_array = [self.text_file_path, self.path]
		assert([str(self.text_file_path)] == x.find_matched_files_AND_SEARCH(file_name_array))

	def test_bin_without_option(self):
		print subprocess.check_output('pwd')
		output = subprocess.check_output(['bin/logfind', 'Skeleton'])
		assert('/Users/madelynfreed/Documents/misc/Python/projects/rebuildGrep/texter.txt' in output)
	
	def test_bin_with_OR_argument(self):
		output = subprocess.check_output(['bin/logfind', '-o', 'Skeleton', 'Jeebers'])
		assert('/Users/madelynfreed/Documents/misc/Python/projects/rebuildGrep/palumbo.txt' in output)

