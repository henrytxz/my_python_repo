class Matrix(object):
  """
  docstring
  """
  def __init__(self, size):
    """
    referenced
    http://stackoverflow.com/questions/12791501/python-initializing-a-list-of-lists
    """
    self.mat = []
    # row = [0]*size
    for i in range(size):
      self.mat.append([0]*size)

    # # self.mat = [[int(0)]*size]*size
    # for row in size:
    #   for col in size:


  def print_matrix(self):
    print 'matrix:'
    for row in self.mat:
      print row

  def set_cell(self, row, col, value):
    self.mat[row][col] = value

if __name__ == '__main__':
  # m1 = Matrix(1)
  # m1.print_matrix()
  # m1.set_cell(0,0,1)
  # m1.print_matrix()

  m2 = Matrix(2)
  m2.print_matrix()
  m2.set_cell(0,0,1)
  m2.print_matrix()

# Foo.assert_equals(spiralize(1), [[1]])
#   Foo.assert_equals(spiralize(2), [[1,1],
#                                    [0,1]])
  # Test.assert_equals(spiralize(3), [[1,1,1],
  #                                   [0,0,1],
  #                                   [1,1,1]])
