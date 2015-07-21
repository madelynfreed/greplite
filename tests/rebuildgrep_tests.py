from nose.tools import *
from rebuildgrep import walk
import os

class TestClass():

	def setup(self):
		file_extensions = ['\.log','\.txt','\.py']	
		self.path = os.path.join(os.path.expanduser('~'), '.hooligans')
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
		x = walk.Recurse('_')
		self.f = open(self.path, 'r')
		assert_false(x.take_file_return_list(self.f) == [])
		self.f.close()

	def teardown(self):
		os.remove(self.path)

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
		x = walk.Recurse('_')
		self.f = open(self.path, 'r')
		assert_false(x.take_file_return_list(self.f) == [])
		self.f.close()

