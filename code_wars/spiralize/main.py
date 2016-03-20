# from matrix import Matrix
from direction import Direction, Right, Up

def spiralize(size):
    mat = [[0]*size for i in range(size)]
    mat[0][0] = 1
    # direction = 'r'
    go_algo = Go(mat, (0,0), Right())
    while not go_algo.done():
        go_algo.keep_going_in_1_direction()
    return mat

class Go(object):
    def __init__(self, mat, curr_pos, direction):
        """

        :param mat:
        :param curr_pos:  a pair tuple
        :param direction:
        :return:
        """
        self.mat = mat
        self.curr_pos = curr_pos
        # self.hypothetical_pos = curr_pos
        self.direction = direction
        self.direction_and_number_steps = {}
        self.number_steps_in_direction = 0

    def switch_direction(self):
        self.direction = self.direction.change_direction()
        self.direction_and_number_steps[str(self.direction)] = self.number_steps_in_direction
        return True

    def done_with_direction(self):
        hypothetical_pos = self.direction.step(self.curr_pos)
        if self.out_of_bound(hypothetical_pos):
            return self.switch_direction()

        # if taking 2 steps would overlap another point of the spiral => done
        hypothetical_pos = self.direction.step(hypothetical_pos)
        row, col = hypothetical_pos
        if not self.out_of_bound(hypothetical_pos) \
                and self.mat[row][col] == 1:
            return self.switch_direction()



        return False

    def keep_going_in_1_direction(self):
        while not self.done_with_direction():
            self.step()

    def done(self):
        # if the algo wasn't able to step in the last direction,
        # that means it's done
        try:
            return self.direction_and_number_steps.values()[-1]==0
        except:
            return len(self.mat)==1

    def step(self):
        row, col = self.curr_pos
        self.mat[row][col] = 1  # mark as visited
        new_pos = self.direction.step(self.curr_pos)
        print 'going from {0} to {1}'.format(self.curr_pos, new_pos)
        self.curr_pos = new_pos
        self.number_steps_in_direction += 1

    def out_of_bound(self, hypothetical_pos):
        row, col = hypothetical_pos
        if row >= len(self.mat) or row<0: return True
        if col >= len(self.mat) or col<0: return True
        return False

class Validate(object):
  @staticmethod
  def assert_equals(x, y):
    try:
        assert x==y
    except:
        print 'assert failed'
        print 'Produced:'
        print_list_of_lists(x)
        print 'Expected:'
        print_list_of_lists(y)
        print '='*88

def make_matrix(size):
    return [[0]*size for i in range(size)]

def print_list_of_lists(ll):
    print 'matrix:'
    for row in ll:
      print row


      
if __name__ == '__main__':
    m2 = make_matrix(size=2)
    assert Go(m2, (0,0), Right()).done_with_direction() is False
    assert Go(m2, (0,1), Right()).done_with_direction() is True
    m3 = [[1,1,1],
          [0,0,1],
          [1,1,1]]
    assert Go(m3, (2,0), Up()).done_with_direction() is True
    # assert Go(m2, (0,1), Up()).done_with_direction() is True

    Validate.assert_equals(spiralize(1), [[1]])
    Validate.assert_equals(spiralize(2), [[1,1],
                                          [0,1]])
    # Validate.assert_equals(spiralize(3), [[1,1,1],
    #                                       [0,0,1],
    #                                       [1,1,1]])
    # Validate.assert_equals(spiralize(5), [[1,1,1,1,1],
    #                                   [0,0,0,0,1],
    #                                   [1,1,1,0,1],
    #                                   [1,0,0,0,1],
    #                                   [1,1,1,1,1]])
    # Validate.assert_equals(spiralize(8), [[1,1,1,1,1,1,1,1],
    #                                   [0,0,0,0,0,0,0,1],
    #                                   [1,1,1,1,1,1,0,1],
    #                                   [1,0,0,0,0,1,0,1],
    #                                   [1,0,1,0,0,1,0,1],
    #                                   [1,0,1,1,1,1,0,1],
    #                                   [1,0,0,0,0,0,0,1],
    #                                   [1,1,1,1,1,1,1,1]])
    
    
    
    
