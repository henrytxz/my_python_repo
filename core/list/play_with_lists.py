l = [1,2,3]
print "the 1st element is:", l[0]
print "the 2nd element is:", l[1]
print "the 3rd element is:", l[2]

print max(l)

def average(l):
	return sum(l)/float(len(l))
print 'average: {0}'.format(average(l))

l2 = [3,5,1]
sorted_l2 = sorted(l2)
l2.sort()
assert sorted_l2 == l2

l.reverse()
assert l == [3,2,1]

l.remove(2)
assert l == [3,1]
