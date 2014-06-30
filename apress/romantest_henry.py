'''
Unit tests for roman.py
written by Henry, as an exercise
'''

import roman
import unittest

class KnownValues2(unittest.TestCase):
	knownValues = ( (1,'I'),
					(2,'II'),
					(3,'III'),
					(10,'X'),
					(50,'L'),
					(100,'C') )
	
	def testToRomanKnownValues(self):
		'''toRoman should give known result with correct input'''
		for integer, numeral in self.knownValues:
			result=roman.toRoman(integer)
			self.assertEqual(numeral, result)
			
	
