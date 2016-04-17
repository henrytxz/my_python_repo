#---------------
# User Instructions
#
# Complete the search and match functions. Match should
# match a pattern only at the start of the text. Search
# should match anywhere in the text.

def search(pattern, text):
    "Match pattern anywhere in text; return longest earliest match or None."
    for i in range(len(text)):
        m = match(pattern, text[i:])
        if m is not None:
            return m

def match(pattern, text):
    "Match pattern against start of text; return longest match found or None."
    remainders = matchset(pattern, text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:(len(text)-len(shortest))]

def components(pattern):
    "Return the op, x, and y arguments; x and y are None if missing."
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y

def matchset(pattern, text):
    "Match pattern at start of text; return a set of remainders of text."
    op, x, y = components(pattern)
    if 'lit' == op:
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        return matchset(x, text) | matchset(y, text)
    elif 'dot' == op:
        return set([text[1:]]) if text else null
    elif 'oneof' == op:
        # A most concise
        return set([text[1:]]) if (text and text[0] in set(x)) else null
        # B i came up with this, also works
        # return set([text[1:]]) if (text.startswith(c) for c in set(x)) else null
        # C expand it more also works:
        # chars = set(x); res = set()
        # for char in chars:
        #     res = res | (set([text[1:]]) if text.startswith(char) else null)
        # return res
    elif 'eol' == op:
        return set(['']) if text == '' else null
    elif 'star' == op:
        return (set([text]) |
                set(t2 for t1 in matchset(x, text)
                    for t2 in matchset(pattern, t1) if t1 != text))
    else:
        raise ValueError('unknown pattern: %s' % pattern)

null = frozenset()

def lit(string):  return ('lit', string)

# def seq(x, *args):
#     if len(args)==1:
#         return ('seq', x, args[0])
#     elif len(args)==0:
#         return x
#     else:
#         return seq(x, seq(args[0], *args[1:]))
#         # Note: it's important to have the * here because I want to pass in len(list)!!! arguments, not list as 1 argument

def seq(x, y): return ('seq', x, y)

# def n_ary(bin_f):
#     def f(*args):
#         if len(args)==1:
#             return args[0]
#         elif len(args)==2:
#             return bin_f(*args)
#         else:
#             return bin_f(args[0], f(*args[1:]))
#     return f

def alt(x, y):    return ('alt', x, y)
def star(x):      return ('star', x)
def plus(x):      return seq(x, star(x))
def opt(x):       return alt(lit(''), x)
def oneof(chars): return ('oneof', tuple(chars))
dot = ('dot',)
eol = ('eol',)

def n_ary(bin_f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x.
    Why it works, unpacks 1 pattern from *args at a time then recurse
    the base case is when len(args) is 0, return x
    """
    def n_ary_f(x, *args):
        return x if len(args)==0 else bin_f(x, n_ary_f(*args))
    return n_ary_f

def run():
    # matchset(abc, abcde) should return set(['de'])
    assert match(seq(lit('a'),lit('b')), 'abcde') == 'ab'
    assert n_ary(seq)(lit('a')) == ('lit', 'a')
    assert match(n_ary(seq)(lit('a')), 'abcde') == 'a'
    assert match(n_ary(seq)(lit('a'),lit('b')), 'abcde') == 'ab'
    """
    flow:
    n_ary_seq(lit('a'),lit('b'))
    n_ary_seq(lit('a'), n_ary_seq(lit('b'))) because len(args) is 1 and not 0
    n_ary_seq(lit('a'), lit('b')) because n_ary_seq(lit('b')) len(args) is 0, x is lit('b')
    seq(lit('a'), lit('b')) because when len(args) is 0, n_ary_seq(x, *args) returns x
    seq(lit('a'), lit('b'))(text) returns 'ab' if text.startswith('ab') else None
    """
    assert match(n_ary(seq)(lit('a'),lit('b')), '9834') == None # yes indeedy!
    assert match(n_ary(seq)(lit('a'),lit('b'),lit('c')), 'abcde') == 'abc'

    assert matchset(('oneof', 'ab'), 'aabc123') == set(['abc123'])
    assert match(('oneof', 'ab'), 'aabc123') == 'a'
    assert match(('star', ('lit', 'a')),'aaabcd') == 'aaa'
    assert match(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == None
    assert match(('alt', ('lit', 'b'), ('lit', 'a')), 'ab') == 'a'
    assert search(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == 'b'
    return 'tests pass'

print run()
