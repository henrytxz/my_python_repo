import string

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

def digit():
    """
    a pattern is supposed to return a set of remainders => this is not a pattern just yet
    """
    # return lambda t: (t[0] in word_chars) if t else False
    return lambda t: set([t[1:]]) if t and t[0] in word_chars else null

def wspace():
    """
    a pattern is supposed to return a set of remainders => this is not a pattern just yet
    """
    return lambda t: set([t[1:]]) if (t and t[0] in white_spaces) else null

def seq(x, y):
    return lambda t: set([t2 for t1 in x(t) for t2 in y(t1)])

white_spaces = set([' ','\t'])
word_chars = set(string.digits) | set(string.ascii_letters) | set(['_'])
null = frozenset([])


def test():
    assert digit()('8') == set([''])
    assert digit()('_') == set([''])
    assert digit()('B') == set([''])

    assert seq(lit('5'), lit('6'))('5678') == set(['78'])
    assert seq(lit('5'), star(lit('6')))('566678') == \
           set(['78', '678', '6678', '66678'])

    # from regex import digit, wspace, star
    assert wspace()('  385') == set([' 385'])
    assert star(wspace())('  385') == set(['  385', ' 385', '385'])
    assert match(seq(seq(digit(), star(wspace())), digit()), '3  jilw') == '3  j'

    # re.match('1(x|y)'
    # match = re.search(r'\d\s*\d', 'xx1 2   3xx') would use seq
    #                     seq(seq(digit(), star(wspace()), digit())

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