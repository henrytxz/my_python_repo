# reduce(function, iterable[, initializer])
# Apply function of two arguments cumulatively to the items of iterable,
# from left to right, so as to reduce the iterable to a single value.
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# calculates ((((1+2)+3)+4)+5).
# The left argument, x, is the accumulated value and the right argument, y,
# is the update value from the iterable. If the optional initializer is
# present,
# it is placed before the items of the iterable in the calculation,
# and serves as a default when the iterable is empty.
#
# If initializer is not given and iterable contains only one item,
# the first item is returned. Roughly equivalent to:
#
# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         try:
#             initializer = next(it)
#         except StopIteration:
#             raise TypeError('reduce()
#               of empty sequence with no initial value')
#     accum_value = initializer
#     for x in it:
#         accum_value = function(accum_value, x)
#     return accum_value

add = lambda x,y:x+y

assert reduce(add, [1,2,3])==6

assert reduce(add, [1,2,3], 5)==11
