class Matrix(object):
  """
  a 2D matrix represented by a list of lists
  """
  def __init__(self, size):
    """
    referenced
    http://stackoverflow.com/questions/12791501/python-initializing-a-list-of-lists
    """
    # self.mat = []
    # for i in range(size):
    #   self.mat.append([0]*size)

    self.mat = [[0]*size for i in range(size)]

  def print_matrix(self):
    print 'matrix:'
    for row in self.mat:
      print row

  def get_matrix(self):
    return self.mat

  @staticmethod
  def print_list_of_lists(ll):
    print 'matrix:'
    for row in ll:
      print row

if __name__ == '__main__':
  m1 = Matrix(1)
  mat1 = m1.get_matrix()
  mat1[0][0] = 1
  assert mat1[0][0] == 1

  m2 = Matrix(2)
  mat2 = m2.get_matrix()
  mat2[0][0] = 1
  assert mat2[0][0] == 1
  assert mat2[0][1] == 0
  assert mat2[1][0] == 0
  assert mat2[1][1] == 0
  m2.print_matrix()