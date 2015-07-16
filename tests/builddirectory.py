import os
# import sys
import random

starting_wd = os.getcwd()
x = os.getcwd()

for i in range(10):
	os.mkdir(os.path.join(x,str(i)))
	x = os.path.join(x,str(i))
	print x
	os.chdir(x)
	print os.getcwd()

