# -----------------
# User Instructions
#
# In this problem, you will use a faster version of Pwin, which we will call
# Pwin2, that takes a state as input but ignores whether it is player 1 or
# player 2 who starts. This will reduce the number of computations to about
# half. You will define a function, Pwin3, which will be called by Pwin2.
#
# Pwin3 will only take me, you, and pending as input and will return the
# probability of winning.
#
# Keep in mind that the probability that I win from a position is always
# (1 - probability that my opponent wins).


from functools import update_wrapper
from max_wins import pig_actions, hold, roll


def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError, e:
            # some element of args refuses to be a dict key - when mutable
            print 'type error found {0}!'.format(e)
            return f(args)
    _f.cache = cache
    return _f

goal = 40

def Q_pig(state, action, Pwin2):
    "The expected value of choosing action in state."
    if action == 'hold':
        return 1 - Pwin2(hold(state))
    if action == 'roll':
        return (1 - Pwin2(roll(state, 1))
                + sum(Pwin2(roll(state, d)) for d in (2,3,4,5,6))) / 6.
    raise ValueError

def Pwin2(state):
   """The utility of a state; here just the probability that an optimal player
   whose turn it is to move can win from the current state."""
   _, me, you, pending = state
   return Pwin3(me, you, pending)

@memo
def Pwin3(me, you, pending):
    ## your code here
    """
    careful about inf loop
    handle the case when pending is 0

    memo(Pwin3)(me, you, pending)
    me is the realized score of current player
    you is the other player's realized score
    """
    if me+pending >= goal:
        return 1
    elif you >= goal:
        return 0
    state = (0, me, you, pending)
    # print 'state: {0}'.format(state)
    return max(Q_pig(state, action, Pwin2) for action in pig_actions(state))


def test():
    epsilon = 0.0001 # used to make sure that floating point errors don't cause test() to fail
    assert goal == 40
    assert len(Pwin3.cache) <= 50000
    # assert Pwin2((0, 42, 25, 0)) == 1
    # assert Pwin2((1, 12, 43, 0)) == 0
    # assert Pwin2((0, 34, 42, 1)) == 0
    assert abs(Pwin2((0, 25, 32, 8)) - 0.736357188272) <= epsilon
    assert abs(Pwin2((0, 19, 35, 4)) - 0.493173612834) <= epsilon
    return 'tests pass'

if __name__ == '__main__':
    print test()

