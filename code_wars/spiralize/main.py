# from matrix import Matrix
from direction import Direction, Right, Up

def spiralize(size):
    mat = [[0]*size for i in range(size)]
    mat[0][0] = 1
    # direction = 'r'
    go_algo = Go(mat, (0,0), Right())
    go_algo.run()
    # while not go_algo.done():
    #     go_algo.keep_going_in_1_direction()
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

    def run(self):
        """
        hp stands for hypothetical position
        :return:
        """
        while True:
            hp = self.direction.step(self.curr_pos)
            if self.bad_move(hp):
                self.direction = self.direction.change_direction()
                hp = self.direction.step(self.curr_pos)
                if self.bad_move(hp):
                    break   # 2 bad moves means the end of the spiral
            # print 'going from {0} to {1}'.format(self.curr_pos, hp)
            self.curr_pos = hp
            row, col = self.curr_pos
            self.mat[row][col] = 1

    def bad_move(self, position):
        if self.out_of_bound(position): return True
        num_visited_neighbors = 0
        row, col = position
        num_visited_neighbors += self.check_neighbor_visited((row, col - 1))
        num_visited_neighbors += self.check_neighbor_visited((row, col + 1))
        num_visited_neighbors += self.check_neighbor_visited((row - 1, col))
        num_visited_neighbors += self.check_neighbor_visited((row + 1, col))
        if num_visited_neighbors > 1: return True

    def check_neighbor_visited(self, hp):
        row, col = hp
        if not self.out_of_bound(hp) and self.mat[row][col] == 1:   # todo: draw Venn diagram
            return 1
        return 0

    def out_of_bound(self, hp):
        row, col = hp
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
    # m2 = make_matrix(size=2)
    # assert Go(m2, (0,0), Right()).done_with_direction() is False
    # assert Go(m2, (0,1), Right()).done_with_direction() is True
    # assert Go(m2, (0,0), Right()).out_of_bound()
    #
    # m3 = [[1,1,1],
    #       [0,0,1],
    #       [1,1,1]]
    # assert Go(m3, (2,0), Up()).done_with_direction() is True
    # assert Go(m2, (0,1), Up()).done_with_direction() is True

    Validate.assert_equals(spiralize(1), [[1]])
    print '='*88
    Validate.assert_equals(spiralize(2), [[1,1],
                                          [0,1]])
    print '='*88
    Validate.assert_equals(spiralize(3), [[1,1,1],
                                          [0,0,1],
                                          [1,1,1]])
    print '='*88
    Validate.assert_equals(spiralize(5), [[1,1,1,1,1],
                                      [0,0,0,0,1],
                                      [1,1,1,0,1],
                                      [1,0,0,0,1],
                                      [1,1,1,1,1]])
    print '='*88
    Validate.assert_equals(spiralize(8), [[1,1,1,1,1,1,1,1],
                                      [0,0,0,0,0,0,0,1],
                                      [1,1,1,1,1,1,0,1],
                                      [1,0,0,0,0,1,0,1],
                                      [1,0,1,0,0,1,0,1],
                                      [1,0,1,1,1,1,0,1],
                                      [1,0,0,0,0,0,0,1],
                                      [1,1,1,1,1,1,1,1]])
    print '='*88
