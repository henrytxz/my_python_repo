# -----------------
# User Instructions
#
# Write a function, play_pig, that takes two strategy functions as input,
# plays a game of pig between the two strategies, and returns the winning
# strategy. Enter your code at line 41.
#
# You may want to borrow from the random module to help generate die rolls.

import random

possible_moves = ['roll', 'hold']
other = {1:0, 0:1}
goal = 50

def clueless(state):
    "A strategy that ignores the state and chooses at random from possible moves."
    return random.choice(possible_moves)

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    (p, me, you, pending) = state
    return (other[p], you, me+pending, 0)

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me+1, 0) # pig out; other player's turn
    else:
        return (p, me, you, pending+d)  # accumulate die roll in pending

def roll_a_die():
    return random.choice(range(1,7))

def play_pig(A, B):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    # your code here
    player_to_strategy = {0:A, 1:B}
    p = random.choice((0,1))
    # print '{} will go first'.format(p)
    state = (p, 0, 0, 0)
    while True:
        action = player_to_strategy[p](state)       # strategy maps a state to an action
        if action == 'hold':
            state = hold(state)
        elif action == 'roll':
            d = roll_a_die()
            state = roll(state, d)
        p, me, you, _ = state
        if me >= goal: return player_to_strategy[p]
        if you >= goal: return player_to_strategy[other[p]]

def always_roll(state):
    return 'roll'

def always_hold(state):
    return 'hold'

def test():
    # outcomes = []
    # for i in range(60000):
    #     outcomes.append(roll_a_die())
    # for i in range(1,7):
    #     print '{0} appears {1} times'.format(i, outcomes.count(i))

    # for i in range(10):
    #     play_pig(always_hold, always_roll)

    for _ in range(10):
        winner = play_pig(always_hold, always_roll)
        assert winner.__name__ == 'always_roll'
    return 'tests pass'

print test()


