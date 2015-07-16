import os
# import sys
import random

starting_wd = os.getcwd()
x = os.getcwd()
print starting_wd


for i in range(10):
	os.mkdir(os.path.join(x,str(i)))
	x = os.path.join(x,str(i))
	print x
	os.chdir(x)
	print os.getcwd()



i want to make a arbitrary tree with files in arbitrary nodes