# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the
# non-negative numbers. The runtime of your program should be
# proportional to the LOGARITHM of the input. You may want to
# do some research into binary search and Newton's method to
# help you out.
#
# This function should return another function which computes the
# inverse of the input function.
#
# Your inverse function should also take an optional parameter,
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is
# efficient enough.

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1

def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        l=0.0
        r=100.0
        while f(r) < y:
            r = r*2
            print f(r)
        print 'find good r {0}'.format(r)
        while min(y-f(l), f(r)-y)>pow(10,-6):
            print 'y {0}'.format(y)
            print 'l {0}'.format(l)
            print 'r {0}'.format(r)
            print 'y-f(l): {0}'.format(y-f(l))
            print 'f(r)-y: {0}'.format(f(r)-y)
            if f(r/2)-y<0:
                l = (l+r)/2
                # print 'changing l to {0}'.format(l)
            else:
                r = (l+r)/2
                # print 'changing r to {0}'.format(r)
        print 'y-f(l): {0}'.format(y-f(l))
        print 'f(r)-y: {0}'.format(f(r)-y)
        if (y-f(l)) < (f(r)-y):
            return l
        else:
            return r
    return f_1

def square(x): return x*x
sqrt = inverse(square)

import time
start = time.time()
# print 'sqrt {0}'.format(sqrt(100))
print pow(10,-6)
print 'sqrt {0}'.format(sqrt(1e6))
# print 'sqrt {0}'.format(sqrt(10000000000))
# print sqrt(10000000000)
stop = time.time()
print 'took {0}'.format(stop-start)
