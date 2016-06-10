"""
may be able to further generalize..
"""
from copy import copy

Fail = []


def successors(x, y, X, Y):
    """
    :return a dict of (state : action) that can be reached from (x,y)
    """
    assert x <= X and y <= Y
    return {
        (0,y) : 'empty x',
        (x,0) : 'empty y',
        (X,y) : 'fill x',
        (x,Y) : 'fill y',
        (x-min(x,Y-y), y+min(x,Y-y)) : 'x->y',
        (x+min(y,X-x), y-min(y,X-x)) : 'x<-y'
    }

def waterpour(X, Y, goal, start=('origin', (0,0))):
    """
    concepts:
    explored: the set of states already visited
    frontier: a list of paths
    path: a list of (action, state), path[-1] is the latest (action, state)
    state: a pair (level in jar x, level in jar y)
    :param X:   max level jar x
    :param Y:   max level jar y
    """
    if goal in start:   return start
    explored = set()
    explored.add(start[1])
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        action, state = path[-1]
        d = successors(state[0], state[1], X, Y)
        for state, action in d.iteritems():
            if state not in explored:
                new_path = copy(path)
                new_path.append((action, state))
                if goal in state: return new_path
                else: frontier.append(new_path)
    return Fail


if __name__ == '__main__':
    # test case from Lesson 4
    print waterpour(9, 4, goal=6)


