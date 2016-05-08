"""
may be able to further generalize..
"""

class WaterPouring(object):
    def __init__(self, curr, capacity):
        self.curr = curr
        self.capacity = capacity

    def get_curr(self):
        return self.curr

    # def set_curr(self, curr):
    #     """
    #     method for speeding up testing
    #     """
    #     self.curr = curr
    #     print self.curr

    def fill(self, i):
        self.curr[i] = self.capacity[i]

    def empty(self, i):
        self.curr[i] = 0

    def transfer(self, fr, to):
        total = sum(self.curr)
        self.curr[to] = min(self.capacity[to], total)
        self.curr[fr] = total - self.curr[to]

    # def run(self):

# def init_test_case(curr, capacity):
#     curr =
#     capacity = (9,4)
#     return

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
