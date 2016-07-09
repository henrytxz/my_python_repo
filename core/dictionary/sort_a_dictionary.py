"""
Created on May 25, 2014
"""

import operator

d = {'a':2,'b':1}
sorted_d0 = sorted(d.iteritems(),key=operator.itemgetter(0))
print 'sort by key:'
print sorted_d0

sorted_d1 = sorted(d.iteritems(),key=operator.itemgetter(1))
print 'sort by value:'
print sorted_d1

"""
some people do
sorted_d = sorted(d.items(), key=operator.itemgetter(0 or 1))
http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
"""