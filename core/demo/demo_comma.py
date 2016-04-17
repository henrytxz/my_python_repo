"""
Reference
http://stackoverflow.com/questions/1708292/meaning-of-using-commas-and-underscores-with-python-assignment-operator
comma is the separator for values in a tuple (as well as a list)
"""

tuple3 = (1, 2, 3)
x, y, z = tuple3
assert x == tuple3[0]
# "So 'b,=T' means get the first element from that tuple? Is it synonymous to 'b=T[0]'?"

tuple2 = (1, 2)
x, y = tuple2
assert x == tuple2[0]