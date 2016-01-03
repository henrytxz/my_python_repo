"""
    http://www.python-course.eu/global_vs_local_variables.php
"""

# eg 1
# def f():
#     print s
# s = "I hate spam"
# f()
# outputs "I hate spam"

# eg 2
# def f():
#     s = "Me too."
#     print s
#
# s = "I hate spam."
# f()
# print s
# outputs "Me too."
# then "I hate spam."

# combine eg 1 and 2
# def f():
# 	print s
# 	s = "Me too."
# 	print s
#
#
# s = "I hate spam."
# f()
# print s
# outputs "UnboundLocalError: local variable 's' referenced before assignment"

# now if we are explicit
def f():
    global s
    print s
    s = "That's clear."
    print s

s = "Python is great!"
f()
print s
# outputs "Python is great!"
# then "That's clear."
# then "That's clear."

