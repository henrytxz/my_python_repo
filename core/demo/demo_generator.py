total = 0
for i in xrange(10):
    total += i
assert total == sum(i for i in xrange(10))

g = (i for i in xrange(10))
assert 'generator' in str(type(g))

assert g.next()==0
assert g.next()==1
assert g.next()==2

