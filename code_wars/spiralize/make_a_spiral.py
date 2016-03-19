

"""
keep_going = {
    'r': lambda (i,j),size,mat : j<size and mat[],
    'd':,
    'l':,
    'u':,
}"""

def keep_going(mat, curr_pos, last_dir):
    direction = next_direction(last_dir)
    if  direction == 'r' or direction == 'l' :
        dim_to_modify = 1    # the 1st dim is the column
    elif direction == 'u' or direction == 'd' :
        dim_to_modify = 0    # the 0th dim is the row
    else:
        raise Exception('wrong direction {0} specified!'.format(direction))



def going_right_done(mat, curr):
    if curr[1]==mat_dim: return True
    if mat[curr[0], curr[1]+2]==1: return True
    return False

def going_down_done(mat, curr):
    if curr[0]==mat_dim: return True
    if curr[0]+2<=mat_dim and mat[curr[0]+2, curr[1]]==1: return True

def going_left_done(mat, curr):
    if curr[1]==0: return True
    if mat[curr[0], curr[1]-2]==1: return True

def going_up_done(mat, curr):
    if curr[1]==mat_dim: return True
    if mat[curr[0]-2, curr[1]]==1: return True



def init_starting_point(curr_col, curr_row, mat):
  print 'curr_row {0}, curr_col {1}'.format(curr_row, curr_col)
  print 'mat[curr_row] {0}'.format(mat[curr_row])
  print 'mat[curr_row][curr_col] {0}'.format(mat[curr_row][curr_col])
  mat[curr_row][curr_col] = 1
  print 'mat[curr_row][curr_col] {0}'.format(mat[curr_row][curr_col])

def spiralize(size):
    # init mat
    mat = [[0]*size]*size
    # print mat
    curr_row, curr_col = 0,0
    init_starting_point(curr_col, curr_row, mat)
    bar = Go(mat, curr_row, curr_col, last_dir=None)
    return bar.get_matrix()

class Go:
  directions = ['r','d','l','u']

  def __init__(self, mat, curr_row, curr_col, last_dir):
    self.mat = mat
    self.curr_row = curr_row
    self.curr_col = curr_col
    self.last_dir = last_dir
    while not self.done():
      self.keep_going()

  def get_matrix(self):
    return self.mat

  def done(self):
    return True
    # direction = next_direction(last_dir)
    # mat_dim = len(mat)
    # if direction == 'r' and (

  @classmethod
  def next_direction(self, last_dir):
    if last_dir == None: # this is true at move 0
        return Go.directions[0]
    return Go.directions[(Go.directions.index(last_dir)+1)%4]

  def keep_going(self):
    pass


class Foo:
  @staticmethod
  def assert_equals(x, y):
    try:
      assert x==y
    except:
      print 'assert failed'
      print 'x:{0}'.format(x)
      print 'y:{0}'.format(y)

if __name__ == '__main__':
  assert Go.next_direction(None) == 'r'
  assert Go.next_direction('r') == 'd'
  assert Go.next_direction('d') == 'l'
  assert Go.next_direction('l') == 'u'
  assert Go.next_direction('u') == 'r'

  # Foo.assert_equals(spiralize(1), [[1]])
  Foo.assert_equals(spiralize(2), [[1,1],
                                   [0,1]])
  # Test.assert_equals(spiralize(3), [[1,1,1],
  #                                   [0,0,1],
  #                                   [1,1,1]])
  # Test.assert_equals(spiralize(5), [[1,1,1,1,1],
  #                                   [0,0,0,0,1],
  #                                   [1,1,1,0,1],
  #                                   [1,0,0,0,1],
  #                                   [1,1,1,1,1]])
  # Test.assert_equals(spiralize(8), [[1,1,1,1,1,1,1,1],
  #                                   [0,0,0,0,0,0,0,1],
  #                                   [1,1,1,1,1,1,0,1],
  #                                   [1,0,0,0,0,1,0,1],
  #                                   [1,0,1,0,0,1,0,1],
  #                                   [1,0,1,1,1,1,0,1],
  #                                   [1,0,0,0,0,0,0,1],
  #                                   [1,1,1,1,1,1,1,1]])
