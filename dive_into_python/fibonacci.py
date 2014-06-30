#!/usr/bin/env python

def fib(n):
	'''
	fibonacci
	Listing 2-6 from the book
	'''

	#print 'n=', n
	if n>1:
		return n*fib(n-1)
	else:
	#	print 'end of the line'
		return 1

print "fib(1):", fib(1)
print "fib(3):", fib(3)

