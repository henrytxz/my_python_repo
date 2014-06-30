import unittest

class test(unittest.TestCase):
	
	def test(self):
		d = {1:'a', 2:'b'}
		for foo, bar in d.iteritems():	#it doesn't have to be key, value :)
			print "key: ", foo, " value: ", bar