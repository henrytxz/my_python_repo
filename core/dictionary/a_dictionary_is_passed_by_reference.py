#!/usr/bin/env python

def a_dictionary_is_passed_by_reference():
	a_dictionary={}
	func(a_dictionary)
	print "dictionary contains: %r" % a_dictionary
	
def func(a_dictionary):
	a_dictionary['key']="value"
	
a_dictionary_is_passed_by_reference()
