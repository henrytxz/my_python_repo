from functools import update_wrapper

def decorator(d):
    def _d(g):
        return update_wrapper(d(g), g) # docstring of seq gets passed to n_ary_f
    update_wrapper(_d, d)     # docstring of n_ary_f gets passed to decorator
    return _d
"""
what happened here was
d  is n_ary
g  is seq
d(g) is n_ary_f
without update_wrapper, n_ary_f doesn't have the docstring of seq
after update_wrapper(f(g), g), n_ary_f has the docstring of seq
in other words, d is such that when g is seq, d will have the docstring of seq
we need to do that for _d, _d needs the docstring of d so it has the docstring of g
"""

@decorator
def n_ary(f):
    """
    Given binary function f(x, y), return an n_ary function such that
    f(x,y,x) = f(x, f(y,z)), etc. Also allow f(x) = x.
    """
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f

@n_ary
def seq(x,y):
    """ docstring of the seq function """
    return ('seq',x,y)

help(seq)