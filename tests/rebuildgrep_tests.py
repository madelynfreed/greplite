#set up tests that set up a file structure with some negative examples

from nose.tools import *
from rebuildgrep import walk

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
	assert(x.is_log_file("bloggy.py"))

def test_is_not_log_file():
	x = walk.Recurse('_')
	assert_false(x.is_log_file("blgy.py"))

def test_find_matching_filenames():
	pass

def test_find_matched_files():
	pass