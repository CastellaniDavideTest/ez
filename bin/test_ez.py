"""Test ez file
"""
from ez import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2021-1-4"

def test():
	"""Tests the ez function in the ez class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert ez.ez() == "ez", "test failed"
	#assert ez.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
