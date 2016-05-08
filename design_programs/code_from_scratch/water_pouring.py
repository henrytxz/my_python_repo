"""
may be able to further generalize..
"""
from copy import copy

class WaterPouring(object):
    def __init__(self, capacity, goal):
        self.capacity = capacity
        self.goal = goal
        self.goal_reached = False
        self.solution = []
        self.visited = []

    def fill(self, curr, i):
        result = copy(curr)
        result[i] = self.capacity[i]
        return result

    def empty(self, curr, i):
        result = copy(curr)
        result[i] = 0
        return result

    def transfer(self, curr, fr, to):
        result = copy(curr)
        total = sum(curr)
        result[to] = min(self.capacity[to], total)
        result[fr] = total - result[to]
        return result

    def goal_found(self, curr):
        for level in curr:
            if level == self.goal: return True
        return False

    def search(self, curr):
        self.visited.append(curr)
        if self.goal_found(curr):
            self.goal_reached = True
            self.solution.insert(0, copy(curr))
            return
        for state in self.get_neighbors(curr):
            self.search(state)
            if self.goal_reached:
                self.solution.insert(0, curr)
                return

    def get_neighbors(self, curr):
        """
        usually dfs handles checking if a neighbor has already been visited
        here in this class this method does that handling
        in other words, this method only returns not yet visited neighbors
        """
        def fill0(curr): return self.fill(curr, 0)
        def fill1(curr): return self.fill(curr, 1)
        def empty0(curr): return self.empty(curr, 0)
        def empty1(curr): return self.empty(curr, 1)
        def transfer0(curr): return self.transfer(curr, 0,1)
        def transfer1(curr): return self.transfer(curr, 1,0)
        for action in (fill0, fill1, empty0, empty1, transfer0, transfer1):
            if self.goal_reached:
                return
            neighbor = action(curr)
            if neighbor not in self.visited:
                yield neighbor

if __name__ == '__main__':
    # a simple test case
    test_case = WaterPouring(capacity=(9,4), goal=9)
    test_case.search([0,4])
    print '{0} \n has LENGTH {1}!'.format(test_case.solution, len(test_case.solution))

    # test case from Lesson 4
    test_case0 = WaterPouring(capacity=(9,4), goal=6)
    test_case0.search([0,0])
    print '{0} \n has LENGTH {1}!'.format(test_case0.solution, len(test_case0.solution))

    # test get_neighbors
    test_case0 = WaterPouring(capacity=(9,4), goal=6)
    g = test_case0.get_neighbors([6,4])
    assert next(g)==[9,4]
    assert next(g)==[6,4]
    assert next(g)==[0,4]
    assert next(g)==[6,0]

    # test the other actions
    test_case1 = WaterPouring(capacity=(9,4), goal=6)
    assert test_case1.fill([6,1], 1) == [6,4]
    test_case2 = WaterPouring(capacity=(9,4), goal=6)
    assert test_case2.transfer([6,4], 1, 0) == [9,1]
    test_case3 = WaterPouring(capacity=(9,4), goal=6)
    assert test_case3.transfer([6,2], 0, 1) == [4,4]

