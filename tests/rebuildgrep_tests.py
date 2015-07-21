from nose.tools import *
from rebuildgrep import walk
import os

class TestClass():

	def test_is_log_file(self):
		x = walk.Recurse('_')
		assert(x.is_log_file("gorp.log"))

	def test_is_not_log_file(self):
		x = walk.Recurse('_')
		assert_false(x.is_log_file("blgy.py"))

	def test_is_close_but_not_log_file(self):
		x = walk.Recurse('_')
		assert_false(x.is_log_file("blog.lo"))

	def test_logfind_file_exists_empty(self):

		path = os.path.join(os.path.expanduser('~'), 'file_that_exists')
		f = open(path, 'w+')
		x = walk.Recurse('_')
		assert(x.take_file_return_list(f) == [])
		f.close()
		os.remove(path)

	def test_logfind_file_exists_with_regexes(self):
		file_extensions = ['\.log','\.txt','\.py']	
		path = os.path.join(os.path.expanduser('~'), '.logfind')
		f = open(path, 'r+')
		for string in file_extensions:
			print string
			f.write(string + '\n')
		print f.readlines()
		x = walk.Recurse('_')
		assert_false(x.take_file_return_list(path) == [])
		os.remove(path)

