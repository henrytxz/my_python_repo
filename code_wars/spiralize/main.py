from matrix import Matrix
from direction import Direction

def spiralize(size):
    mat = Matrix(size).get_matrix()
    mat[0][0] = 1
    direction = 'r'
    go_algo = Go(mat, (0,0), direction)
    while not Go.done(mat, (0,0), direction):
        go_algo.keep_going_in_1_direction()
    return mat
    
class Go(object):
    def __init__(self, mat, curr_pos, direction):
        self.mat = mat
        self.curr_pos = curr_pos
        self.direction = direction

    def __done_with_direction(self):
        return True

    def keep_going_in_1_direction(self):
        while not self.__done_with_direction():
            self.step()

    @staticmethod   #todo probably make instance method
    def done(mat, curr_pos, direction):
        return True

    def step(self):
        pass


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
      # y.print_matrix()
      # print 'x:{0}'.format(x)
      # print 'y:{0}'.format(y)
      
      
if __name__ == '__main__':
  Validate.assert_equals(spiralize(1), [[1]])
  Validate.assert_equals(spiralize(2), [[1,1],
                                        [0,1]])
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
    
    
    
    
