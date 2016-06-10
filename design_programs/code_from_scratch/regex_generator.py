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
    set_t = set([t])
    return lambda Ns: set_t if len(t) in Ns else null

def alt(x, y):
    return lambda Ns: x(Ns) | y(Ns)

def oneof(chars):
    """
    oneof(abc) => {a, b, c}, this requires 1 to be in Ns
    """
    set_chars = set(chars)
    return lambda Ns: set_chars if 1 in Ns else null

# def star(x):
#     def f(Ns):
#         pass
#     return f

null = frozenset([])

def genseq(x,y,Ns):
    Nss = range(max(Ns)+1)
    return set(m1+m2
               for m1 in x(Nss) for m2 in y(Nss)
               if len(m1+m2) in Ns)

def run():
    assert genseq(lit('a'), lit('b'), set([2])) == set(['ab'])
    # Nss = 0,1,2
    # lit('a')([0 to 2]) = set(['a'])
    # ...
    # seems ok

    # what about
    assert genseq(lit('xyz'), lit('bdk'), set([2])) == set(['ab'])
    # lit('xyz')([0 to 2]) == null
    # ...
    # seems ok

    # what about
    # genseq(a, a*)


    # i = seq(lit('1'), alt('x', 'y'))
    # assert i()

    f = lit('hello')
    assert f(set([1, 2, 3, 4, 5])) == set(['hello'])
    assert lit('hello')(set([1, 2, 3, 4, 5])) == set(['hello'])
    # == re.generate('hello', set([1, 2, 3, 4, 5])) == hello
    assert f(set([1, 2, 3, 4]))    == null

    g = alt(lit('hi'), lit('bye'))
    assert g(set([1, 2, 3, 4, 5, 6])) == set(['bye', 'hi'])
    # == re.generate('hi|bye', set([1, 2, 3, 4, 5, 6]))
    assert g(set([1, 3, 5])) == set(['bye'])

    h = oneof('theseletters')
    assert h(set([1, 2, 3])) == set(['t', 'h', 'e', 's', 'l', 'r'])
    assert h(set([2, 3, 4])) == null

    import re
    assert re.match('he', 'hello') is not None
    assert re.match('a|b', 'abc') is not None
    assert re.match('a|b', 'bcd') is not None
    assert re.match('a|b', 'dcb') is None
    assert re.search('a|b', 'dcb') is not None
    assert re.search('he', 'hello') is not None
    assert re.search('a|b', 'abc') is not None
    assert re.search('a|b', 'bcd') is not None

    return 'tests pass'

print run()
