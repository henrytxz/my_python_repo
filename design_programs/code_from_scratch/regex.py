def match(pattern, string):
    """
    returns the longest substring of string that fits the pattern
    """
    set_remainders = pattern(string)
    if not set_remainders: return None
    shortest_remainder = min(set_remainders, key=len)
    return string[:len(string)-len(shortest_remainder)]

def lit(s):
    return lambda t : set([t[len(s):]]) if t and t.startswith(s) else null

def star(x):
    return lambda t: set([t]) | set([t2 for t1 in x(t) for t2 in star(x)(t1)
                                     if (t and t1!=t)])

def starr(x):
    """
    another way of implementing the star pattern
    """
    def f(t):
        s = set([t])
        for t1 in x(t):
            if t1!=t:
                s = s.union(starr(x)(t1))
        return s
    return f

def oneof(string):
    """
    I'm unclear about the specification for this one at the moment will leave
    it out
    """
    pass

null = frozenset([])

def test():
    assert star(lit('a'))('aabc') == set(['aabc', 'abc', 'bc'])
    assert starr(lit('a'))('aabc') == set(['aabc', 'abc', 'bc'])
    assert match(lit('a'), 'aabc') == 'a'
    assert match(lit('a'), 'bc') == None
    assert match(star(lit('a')), 'aabc') == 'aa'
    assert match(star(lit('a')), 'aaaaabbbaa') == 'aaaaa'
    assert match(starr(lit('a')), 'aabc') == 'aa'
    assert match(starr(lit('a')), 'aaaaabbbaa') == 'aaaaa'
    assert match(lit('hello'), 'hello how are you?') == 'hello'
    assert match(lit('x'), 'hello how are you?') == None
    # assert match(oneof('xyz'), 'x**2 + y**2 = r**2') == 'x'
    # assert match(oneof('xyz'), '   x is here!') == None
    return 'tests pass'

print test()