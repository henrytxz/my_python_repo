#!/usr/bin/env python

def a_dictionary_is_passed_by_reference():
	a_dictionary={}
	func(a_dictionary)
	print "dictionary contains: %r" % a_dictionary
	
def func(a_dictionary):
	a_dictionary['key']="value"
	
	
def a_number_is_passed_by_value():
	bar=1
	change_a_number(bar)
	print "the resulting number is %d" % bar
	
def change_a_number(a_number):
	a_number=2
	
	
a_dictionary_is_passed_by_reference()
a_number_is_passed_by_value()