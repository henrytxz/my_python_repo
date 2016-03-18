directions = ['r','d','l','u']

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

def next_direction(last_dir):
    if last_dir == None: # this is true at move 0
        return directions[0]
    return directions[(directions.index(last_dir)+1)%4]

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

def done(mat, curr, last_dir):
    if last_dir==None: # this is true at move 0
        return False
    else:
        direction = next_direction(last_dir)
        mat_dim = len(mat)
        # if direction == 'r' and (

def spiralize(size):
    # Make a snake
    mat = [[0]*size]*size
    print mat
    curr = [0,0]
    # dir = 'r' # go right first
    # go right till u have to turn then go down till u turn left, etc.
    # while possible, keep going
    # while not done(mat, curr, last_dir):
    #     new = keep_going(mat, curr, last_dir)
    return mat

class Test:
  @staticmethod
  def assert_equals(x, y):
    assert x==y

if __name__ == '__main__':
  assert next_direction(None) == 'r'
  assert next_direction('r') == 'd'
  assert next_direction('d') == 'l'
  assert next_direction('l') == 'u'
  assert next_direction('u') == 'r'

  Test.assert_equals(spiralize(1), [[1]])
  # Test.assert_equals(spiralize(2), [[1,1],
  #                                   [0,1]])
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
