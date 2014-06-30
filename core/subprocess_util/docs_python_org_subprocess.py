'''
Created on May 13, 2014

@author: henry
'''

import unittest
#import csv
import subprocess

class try_subprocess(unittest.TestCase):
	
	def test(self):
		#returncode = 
		subprocess.call(["ls", "-l"])
		#print returncode