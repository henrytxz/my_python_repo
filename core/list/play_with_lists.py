import numpy
import unittest

l = [1,2,3]
# access elements by index
print "the 1st element is:", l[0]
print "the 2nd element is:", l[1]
print "the 3rd element is:", l[2]

# access elements
assert l[len(l)-1] == l[-1]
assert l[:len(l)] == l
# slicing, list[begin:end] includes begin but not end
assert l[0:2] == [1,2]
# and has length end - begin
assert len(l[0:2]) == 2
assert len(l[1:2]) == 1

# find max
assert max(l) == 3

# average value of a list
def average(l):
  return sum(l)/float(len(l))
assert average(l) == 2.0
assert numpy.mean(l) == 2.0

# sort a list
l2 = [3,5,1]
sorted_l2 = sorted(l2)
l2.sort()
assert sorted_l2 == l2

# reverse a list
l.reverse()
assert l == [3,2,1]

# remove an element from the list
l = l+[2]
assert l == [3,2,1,2]
l.remove(2)
assert l == [3,1,2]

# all returns True if all elements of the iterable is True
# any returns True if any element  in the iterable is True
a = ['abc',3]
b = ['abc',3]
c = ['Abc', 3]
assert all([ea==eb for ea,eb in zip(a,b)])
assert not all([ea==eb for ea,eb in zip(a,c)])  # because 'abc' != 'Abc'
assert any([ea==eb for ea,eb in zip(a,c)])      # because 3 == 3