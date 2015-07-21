from nose.tools import *
from rebuildgrep import walk
import os

def setup():
	print "setup"	

def teardown():
	print "TEAR DOWN"

def test_basic():
	print "I RAN"

def test_includes_string():
	pass

def test_is_log_file():
	x = walk.Recurse('_')
	assert(x.is_log_file("gorp.log"))

def test_is_not_log_file():
	x = walk.Recurse('_')
	assert_false(x.is_log_file("blgy.py"))

def test_is_close_but_not_log_file():
	x = walk.Recurse('_')
	assert_false(x.is_log_file("blog.lo"))

def test_logfind_file_exists_empty():

	path = os.path.join(os.path.expanduser('~'), 'file_that_exists')
	f = open(path, 'w+')
	x = walk.Recurse('_')
	assert(x.take_file_return_list(f) == [])
	f.close()
	os.remove(path)

def test_logfind_file_exists_with_regexes():
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

def test_find_matching_filenames():
	pass

def test_find_matched_files():
	pass
