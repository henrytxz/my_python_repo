# -----------------
# User Instructions
#
# In this problem, we introduce doubling to the game of pig.
# At any point in the game, a player (let's say player A) can
# offer to 'double' the game. Player B then has to decide to
# 'accept', in which case the game is played through as normal,
# but it is now worth two points, or 'decline,' in which case
# player B immediately loses and player A wins one point.
#
# Your job is to write two functions. The first, pig_actions_d,
# takes a state (p, me, you, pending, double), as input and
# returns all of the legal actions.
#
# The second, strategy_d, is a strategy function which takes a
# state as input and returns one of the possible actions. This
# strategy needs to beat hold_20_d in order for you to be
# marked correct. Happy pigging!

import random
from max_wins import memo

def pig_actions_d(state):
    """The legal actions from a state. Usually, ["roll", "hold"].
    Exceptions: If double is "double", can only "accept" or "decline".
    Can't "hold" if pending is 0.
    If double is 1, can "double" (in addition to other moves).
    (If double > 1, cannot "double").
    """
    # state is like before, but with one more component, double,
    # which is 1 or 2 to denote the value of the game, or 'double'
    # for the moment at which one player has doubled and is waiting
    # for the other to accept or decline
    (p, me, you, pending, double) = state
    # your code here
    d = {1 :      ['roll','hold','double'],
         2 :      ['roll','hold'],
         'double':['accept','decline']}
    actions = d[double]
    if not pending and double!='double':
        actions.remove('hold')
    return actions

## No more roll() and hold(); instead, do:

def do(action, state, dierolls):
    """Return the state that results from doing action in state.
     If action is not legal, return a state where the opponent wins.
    Can use dierolls if needed."""
    (p, me, you, pending, double) = state
    if action not in pig_actions_d(state):
        return (other[p], goal, 0, 0, double)
    elif action == 'roll':
        d = next(dierolls)
        if d == 1:
            return (other[p], you, me+1, 0, double) # pig out; other player's turn
        else:
            return (p, me, you, pending+d, double)  # accumulate die in pending
    elif action == 'hold':
        return (other[p], you, me+pending, 0, double)
    elif action == 'double':    # from (p, me, you, pending, 1) to
        return (other[p], you, me, pending, 'double')
    elif action == 'decline':
        return (other[p], goal, 0, 0, 1)
    elif action == 'accept':    # from (p, me, you, pending, 'double') to
        return (other[p], you, me, pending, 2)

def Q_pig_d(state, action, U):
    if action == 'hold':
        return 1 - Pwin2(do(action, state, dierolls())) # when action is hold, I know dierolls won't be used so this is not an expectation, it is deterministic
    elif action == 'roll':
        return (1-Pwin2(do(action, state, iter([1,]))) + sum(Pwin2(do(action, state, iter([i,]))) for i in range(2,7)))/6
        # return (sum(Pwin2(do(action, state, iter([i,]))) for i in range(1,7))) / 6
    elif action == 'double':
        # 0, me, you, pending, 'double'
        # same as 1-Pwin2(1, you, me, pending, 2)
        return 1-Pwin2(do(action, state, dierolls()))
    elif action == 'decline':
        return 0.0
    elif action == 'accept':
        return Pwin2(do(action, state, dierolls()))
    else:
        return 0.0

# @memo
# def Pwin_d(state):
#     """The utility of a state; here just the probability that an optimal player
#     whose turn it is to move can win from the current state."""
#     # Assumes opponent also plays with optimal strategy.
#     (p, me, you, pending, double) = state
#     # print 'p {0} me {1} you {2} pending {3}'.format(p, me, you, pending)
#     if me + pending >= goal:
#         return 1
#     elif you >= goal:
#         return 0
#     else:
#         return max(Q_pig_d(state, action, Pwin_d)
#                    for action in pig_actions_d(state))

def best_action(state, actions, Q, U):
    "Return the optimal action for a state, given U."
    def EU(action): return Q(state, action, U)
    return max(actions(state), key=EU)

def strategy_d(state):
    # your code here
    # return best_action(state, pig_actions_d, Q_pig_d, Pwin_d)
    (p, me, you, pending, double) = state
    return ('accept' if double == 'double' else
            'hold' if (pending >= 25 or me + pending >= goal) else
            'roll')

def hold_at(n):
    def f(state):
        (p, me, you, pending, double) = state
        return ('accept' if double == 'double' else
                'hold' if (pending >= n or me + pending >= goal) else
                'roll')
    return f

## You can use the code below, but don't need to modify it.

def hold_20_d(state):
    "Hold at 20 pending.  Always accept; never double."
    (p, me, you, pending, double) = state
    return ('accept' if double == 'double' else
            'hold' if (pending >= 20 or me + pending >= goal) else
            'roll')

def clueless_d(state):
    return random.choice(pig_actions_d(state))

def dierolls():
    "Generate die rolls."
    while True:
        yield random.randint(1, 6)

def play_pig_d(A, B, dierolls=dierolls()):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    strategies = [A, B]
    state = (0, 0, 0, 0, 1)
    while True:
        (p, me, you, pending, double) = state
        if me >= goal:
            return strategies[p], double
        elif you >= goal:
            return strategies[other[p]], double
        else:
            action = strategies[p](state)
            state = do(action, state, dierolls)

goal = 40
other = {1:0, 0:1}

def strategy_compare(A, B, N=1000):
    """Takes two strategies, A and B, as input and returns the percentage
    of points won by strategy A."""
    A_points, B_points = 0, 0
    for i in range(N):
        if i % 2 == 0:  # take turns with who goes first
            winner, points = play_pig_d(A, B)
        else:
            winner, points = play_pig_d(B, A)
        if winner.__name__ == A.__name__:
            A_points += points
        else: B_points += points
    A_percent = 100*A_points / float(A_points + B_points)
    print 'In %s games of pig, strategy %s took %s percent of the points against %s.' % (N, A.__name__, A_percent, B.__name__)
    return A_percent

def test_Pwin_d():
    state = (0, 36, 35, 0, 1)
    assert do('roll', state, iter([1,])) == (1, 35, 37, 0, 1)
    print Pwin_d(do('roll', state, iter([1,])))
    # assert Pwin_d(do('roll', state, iter([2,]))) < 1
    # assert Pwin_d(do('roll', state, iter([3,]))) < 1
    # assert Pwin_d(do('roll', state, iter([4,]))) == 1
    # assert Pwin_d(do('roll', state, iter([5,]))) == 1
    # assert Pwin_d(do('roll', state, iter([6,]))) == 1

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
    state = (0, me, you, pending, 1)
    # print 'state: {0}'.format(state)
    return max(Q_pig_d(state, action, Pwin2) for action in pig_actions_d(state))

def Pwin2(state):
    _, me, you, pending, _ = state
    return Pwin3(me, you, pending)

def double_at(threshold):
    def f(state):
        p, me, you, pending, double = state
        if Pwin3(me, you, pending) > threshold and double==1:
            return 'double'
        else:
            return hold_20_d(state)
    return f

def test():
    # test_Pwin_d()
    # print Q_pig_d((0,0,0,0,1), 'roll', Pwin_d)
    assert set(pig_actions_d((0, 2, 3, 0, 1)))          == set(['roll', 'double'])
    assert set(pig_actions_d((1, 20, 30, 5, 2)))        == set(['hold', 'roll'])
    assert set(pig_actions_d((0, 5, 5, 5, 1)))          == set(['roll', 'hold', 'double'])
    assert set(pig_actions_d((1, 10, 15, 6, 'double'))) == set(['accept', 'decline'])

    # best_record = (0, 0)
    # for x in range(50, 100, 2):
    #     y = strategy_compare(double_at(x/100.0), hold_20_d)
    #     print 'double at {0} wins {1}'.format(x, y)
    #     if y > best_record[1]:
    #         best_record = (x, y)
    # print 'best record is {0}'.format(best_record)

    assert strategy_compare(double_at(94/100.0), hold_20_d) # must win 60% of the points

    return 'test passes'

print test()




