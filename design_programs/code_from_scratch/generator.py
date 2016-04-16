"""
what is a generator?
generator(pattern) produces a a set of strings (a language)
(a|b)(a|b) = {aa, ab, ba, bb}
a* = {'', a, aa, aaa, aaaa, ...}
"""

def lit(t):
    """
    the recognizer lit('a')('abc') = set(['a'])
    in other words, match(a, abc) == a
    we denote a by s and abc by t
    the generator lit('a')(Ns) =
    """
    return lambda Ns: set([t]) if (len(t) in Ns) else null

def alt(x, y):
    return lambda Ns: x(Ns) | y(Ns)

def oneof(chars):
    def f(Ns):
        res = set()
        for char in chars:
            res = res.union(lit(char)(Ns))
        return res
    return f

null = frozenset([])

def test():
    f = lit('hello')
    assert f(set([1, 2, 3, 4, 5])) == set(['hello'])
    assert f(set([1, 2, 3, 4]))    == null

    g = alt(lit('hi'), lit('bye'))
    assert g(set([1, 2, 3, 4, 5, 6])) == set(['bye', 'hi'])
    assert g(set([1, 3, 5])) == set(['bye'])

    h = oneof('theseletters')
    assert h(set([1, 2, 3])) == set(['t', 'h', 'e', 's', 'l', 'r'])
    assert h(set([2, 3, 4])) == null

    return 'tests pass'

print test()
