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
# def seq(x, y):  return ('seq', x, y)
def seq(x, *args):
    if len(args)==1:
        return ('seq', x, args[0])
    elif len(args)==0:
        return lit(x)
    else:
        return seq(x, seq(args[0], *args[1:]))
        #   seq('lit('a')', 'lit('b')', 'lit('c')')
        #           args = ('lit('b')', 'lit('c')')
        #           args[1] = 'lit('c')'
        #           args[1:] = (('lit('c')',))
        #           args =     (('lit('c')',))
        #           len(args) is 1
        #   op, x, y = 'seq', (('lit('c')',)), ''
        #   but

        # suppose we have
        # seq('lit('a')', 'lit('b')', 'lit('c')', 'lit('d')')
        # args = (.., 'lit('d')')
        # args[1:] = (('lit('c')', 'lit('d')')

def alt(x, y):    return ('alt', x, y)
def star(x):      return ('star', x)
def plus(x):      return seq(x, star(x))
def opt(x):       return alt(lit(''), x)
def oneof(chars): return ('oneof', tuple(chars))
dot = ('dot',)
eol = ('eol',)

def run():
    # matchset(abc, abcde) should return set(['de'])
    assert match(seq(lit('a'),lit('b'),lit('c')), 'abcde') == 'abc'
    assert match(seq(lit('a'),lit('b')), 'abcde') == 'ab'
    assert matchset(('oneof', 'ab'), 'aabc123') == set(['abc123'])
    assert match(('oneof', 'ab'), 'aabc123') == 'a'
    assert match(('star', ('lit', 'a')),'aaabcd') == 'aaa'
    assert match(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == None
    assert match(('alt', ('lit', 'b'), ('lit', 'a')), 'ab') == 'a'
    assert search(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == 'b'
    return 'tests pass'

print run()
