from matrix import Matrix
from direction import Direction, Right

def spiralize(size):
    mat = Matrix(size).get_matrix()
    mat[0][0] = 1
    # direction = 'r'
    go_algo = Go(mat, (0,0), Right())
    while not Go.done():
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

    def done_with_direction(self):
        hypothetical_pos = self.direction.step(self.curr_pos)
        if self.out_of_bound(hypothetical_pos):
            self.direction = self.direction.change_direction()
            return True

        # if taking 2 steps would overlap another point of the spiral => done
        hypothetical_pos = self.direction.step(hypothetical_pos)
        row, col = hypothetical_pos
        if not self.out_of_bound(hypothetical_pos) \
                and self.mat[row][col] == 1:
            self.direction = self.direction.change_direction()
            return True

        return False

    def keep_going_in_1_direction(self):
        while not self.done_with_direction():
            self.step()

    @staticmethod   #todo probably make instance method
    def done():
        return True

    def step(self):
        pass

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
        Matrix.print_list_of_lists(x)
        print 'Expected:'
        Matrix.print_list_of_lists(y)
        print '='*88

      
if __name__ == '__main__':
    assert Go(Matrix(2), (0,1), Right()).done_with_direction()


    Validate.assert_equals(spiralize(1), [[1]])
    Validate.assert_equals(spiralize(2), [[1,1],
                                        [0,1]]) # todo get this to pass
    # Validate.assert_equals(spiralize(3), [[1,1,1],
    #                                   [0,0,1],
    #                                   [1,1,1]])
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
    
    
    
    
