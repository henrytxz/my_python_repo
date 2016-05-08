"""
may be able to further generalize..
"""

class WaterPouring(object):
    def __init__(self, curr, capacity, goal):
        self.curr = curr
        self.capacity = capacity
        self.solution = []
        self.visited = set()
        self.goal = goal

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
        
    def search(self):
        for level in self.curr:
            if level == self.goal:
                self.solution.insert(0, self.curr)
                return True # use this as an indicator/sign to collect solution
        for state in self.get_neighbors():
            pass

    def get_neighbors(self):
        def fill0(): self.fill(0)
        def fill1(): self.fill(1)
        def empty0(): self.empty(0)
        def empty1(): self.empty(1)
        def transfer0(): self.transfer(0,1)
        def transfer1(): self.transfer(1,0)
        for action in (fill0, fill1, empty0, empty1, transfer0, transfer1):
            action()
            yield self.curr

if __name__ == '__main__':
    test_case0 = WaterPouring([6,4], capacity=(9,4))
    test_case0.fill(0)
    assert test_case0.get_curr()==[9,4]
    test_case0.empty(0)
    assert test_case0.get_curr()==[0,4]
    test_case0.empty(1)
    assert test_case0.get_curr()==[0,0]

    test_case1 = WaterPouring([6,1], capacity=(9,4))
    test_case1.fill(1)
    assert test_case1.get_curr()==[6,4]

    test_case2 = WaterPouring([6,4], capacity=(9,4))
    test_case2.transfer(1, 0)
    assert test_case2.get_curr()==[9,1]

    test_case3 = WaterPouring([6,2], capacity=(9,4))
    test_case3.transfer(0, 1)
    assert test_case3.get_curr()==[4,4]

