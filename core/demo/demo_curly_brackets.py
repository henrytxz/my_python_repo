x = {1,2,3,3}
assert isinstance(x, set)

y = {'a':1, 'b':2, 'a':3}
assert isinstance(y, dict)
# print y

z = {e for e in range(5)}
assert isinstance(z, set)

print x-frozenset([3])