"""
Reference
http://stackoverflow.com/questions/1708292/meaning-of-using-commas-and-underscores-with-python-assignment-operator

_ is an identifier
it means "I don't care about its value"
"""

tuple3 = (1, 2, 3)
x, _, _ = tuple3
assert x == tuple3[0]

