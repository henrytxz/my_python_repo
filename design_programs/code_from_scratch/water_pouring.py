"""
may be able to further generalize..
"""

class WaterPouring(object):
    def __init__(self, curr, capacity, goal):
        self.curr = curr
        self.capacity = capacity
        self.goal = goal
        self.goal_reached = False
        self.solution = []
        self.visited = []
        self.visited.append(list(curr))

    def get_curr(self):
        return self.curr

    def fill(self, i):
        self.curr[i] = self.capacity[i]

    def empty(self, i):
        self.curr[i] = 0

    def transfer(self, fr, to):
        total = sum(self.curr)
        self.curr[to] = min(self.capacity[to], total)
        self.curr[fr] = total - self.curr[to]

    # def run(self):

    def goal_found(self):
        for level in self.curr:
            if level == self.goal: return True
        return False

    def search(self):
        print self.curr
        if self.goal_found():
            self.goal_reached = True
            print 'inserting self.curr {0}'.format(self.curr)
            self.solution.insert(0, list(self.curr))
            return
        copy_curr_state = list(self.curr)
        for state in self.get_neighbors():
            self.search()
            if self.goal_reached:
                print 'inserting self.curr {0}'.format(copy_curr_state)
                self.solution.insert(0, copy_curr_state)
                return

    def get_neighbors(self):
        """
        usually dfs handles checking if a neighbor has already been visited
        here in this class this method does that handling
        in other words, this method only returns not yet visited neighbors
        """
        def fill0(): self.fill(0)
        def fill1(): self.fill(1)
        def empty0(): self.empty(0)
        def empty1(): self.empty(1)
        def transfer0(): self.transfer(0,1)
        def transfer1(): self.transfer(1,0)
        for action in (fill0, fill1, empty0, empty1, transfer0, transfer1):
            if self.goal_reached:
                return
            copy_curr_state = self.curr
            action()
            if self.curr in self.visited:
                self.curr = copy_curr_state
            else:
                self.visited.append(list(self.curr))
                yield self.curr

if __name__ == '__main__':
    # test_case = WaterPouring([0,4], capacity=(9,4), goal=9)
    # test_case.search()
    # print test_case.solution

    test_case0 = WaterPouring([0,0], capacity=(9,4), goal=6)
    test_case0.search()
    print test_case0.solution

    # test_case0 = WaterPouring([6,4], capacity=(9,4), goal=6)
    # g = test_case0.get_neighbors()
    # assert next(g)==[9,4]
    # assert next(g)==[0,4]
    # assert next(g)==[0,0]
    #
    # test_case1 = WaterPouring([6,1], capacity=(9,4), goal=6)
    # test_case1.fill(1)
    # assert test_case1.get_curr()==[6,4]
    #
    # test_case2 = WaterPouring([6,4], capacity=(9,4), goal=6)
    # test_case2.transfer(1, 0)
    # assert test_case2.get_curr()==[9,1]
    #
    # test_case3 = WaterPouring([6,2], capacity=(9,4), goal=6)
    # test_case3.transfer(0, 1)
    # assert test_case3.get_curr()==[4,4]

