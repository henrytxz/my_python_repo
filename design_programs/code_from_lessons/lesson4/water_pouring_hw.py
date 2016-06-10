# -----------------
# User Instructions
#
# In this problem, you will solve the pouring problem for an arbitrary
# number of glasses. Write a function, more_pour_problem, that takes
# as input capacities, goal, and (optionally) start. This function should
# return a path of states and actions.
#
# Capacities is a tuple of numbers, where each number represents the
# volume of a glass.
#
# Goal is the desired volume and start is a tuple of the starting levels
# in each glass. Start defaults to None (all glasses empty).
#
# The returned path should look like [state, action, state, action, ... ]
# where state is a tuple of volumes and action is one of ('fill', i),
# ('empty', i), ('pour', i, j) where i and j are indices indicating the
# glass number.

# import copy


def more_pour_problem(capacities, goal, start=None):
    """The first argument is a tuple of capacities (numbers) of glasses; the
    goal is a number which we must achieve in some glass.  start is a tuple
    of starting levels for each glass; if None, that means 0 for all.
    Start at start state and follow successors until we reach the goal.
    Keep track of frontier and previously explored; fail when no frontier.
    On success return a path: a [state, action, state2, ...] list, where an
    action is one of ('fill', i), ('empty', i), ('pour', i, j), where
    i and j are indices indicating the glass number."""
    # your code here

    # is_goal = lambda state: (for curr_level in state: if curr_level == goal: True; else: False)

    def done(state):
        for curr_level in state:
            if curr_level == goal:
                return True
        return False

    number_glasses = len(capacities)

    def successors(state):
        """
        the possible actions are: fill, empty, pour
        """
        nexts = {}
        for i in range(number_glasses):
            fill_i = list(state)
            fill_i[i] = capacities[i]
            # nexts[('fill', i)] = fill_i
            nexts[tuple(fill_i)] = ('fill', i)

            empty_i = list(state)
            empty_i[i] = 0
            # nexts[('empty', i)] = empty_i
            nexts[tuple(empty_i)] = ('empty', i)

            for j in range(number_glasses):
                if i==j or state[i]==0 or state[j]==capacities[j]: continue
                amt_transferred = min(state[i], capacities[j]-state[j])
                pour_i_to_j = list(state)
                pour_i_to_j[i] -= amt_transferred
                pour_i_to_j[j] += amt_transferred
                # next[('pour', i, j)] = pour_i_to_j
                nexts[tuple(pour_i_to_j)] = ('pour', i, j)

        return nexts

    start = start if start else [0]*number_glasses
    result = shortest_path_search(start, successors=successors, is_goal=done)
    if result and isinstance(result[0], list):
        result[0] = tuple(result[0])
    return result

    # frontier = []
    # while frontier:
    #     pass
    # return Fail

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set()
    frontier = [ [start] ]
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []

def test_more_pour():
    assert more_pour_problem((1, 2, 4, 8), 4) == [
        (0, 0, 0, 0), ('fill', 2), (0, 0, 4, 0)]
    assert more_pour_problem((1, 2, 4), 3) == [
        (0, 0, 0), ('fill', 2), (0, 0, 4), ('pour', 2, 0), (1, 0, 3)]
    starbucks = (8, 12, 16, 20, 24)
    assert not any(more_pour_problem(starbucks, odd) for odd in (3, 5, 7, 9))
    assert all(more_pour_problem((1, 3, 9, 27), n) for n in range(28))
    assert more_pour_problem((1, 3, 9, 27), 28) == []
    return 'test_more_pour passes'

print test_more_pour()
