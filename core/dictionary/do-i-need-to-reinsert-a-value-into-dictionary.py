#!/usr/bin/env python


def print_dictionary(dictionary):
	print "dictionary contains: %r" % dictionary

def foo():
	a_dictionary={'key':'value'}
	
	value = a_dictionary['key']
	value = 3
	print_dictionary(a_dictionary)
	
	a_dictionary['key'] = 3
	print_dictionary(a_dictionary)
	
	# let's make value a little more interesting, i.e. turn it into a list
	a_dictionary['key'] = [1,2,3]
	print_dictionary(a_dictionary)
	value = a_dictionary['key']
	value = [1,2,4]
	print_dictionary(a_dictionary)
	a_dictionary['key'] = value
	print_dictionary(a_dictionary)
#	func(a_dictionary)
	
	
#def func(a_dictionary):
#	a_dictionary['key']="value"
	
foo()
