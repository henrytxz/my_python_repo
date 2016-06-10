# -----------------
# User Instructions
#
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is
# '->' for here to there or '<-' for there to here. When only one
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.
import itertools

def new_state(state, t0, t1, move):
    here, there, t = state
    fr = here if move=='->' else there
    to = there if move=='->' else here
    new_fr = frozenset({e for e in fr if e not in set(['light', t0, t1])})
    new_to = frozenset(to.union(set([t0, t1, 'light'])))
    if move == '->':
        return (new_fr, new_to, t+max(t0,t1))
    else:
        return (new_to, new_fr, t+max(t0,t1))

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and
    '<-' for there to here."""
    here, there, t = state

    if 'light' in here:
        move = '->'
        fr = {e for e in here if e!='light'}
    else:
        move = '<-'
        fr = {e for e in there if e!='light'}

    d = {}

    for t in fr:
        d[new_state(state, t, t, move)] = (t, t, move)

    for p in itertools.combinations(fr, 2):
        d[new_state(state, p[0], p[1], move)] = (p[0], p[1], move)

    return d

def test():
    # ts = [1, 2, 5, 10]
    # for p in itertools.combinations(ts, 2):
    #     print p

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}

    return 'tests pass'

print test()