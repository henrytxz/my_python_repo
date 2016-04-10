def spiralize(size):
    """
    the idea:
    this problem is made of a data structure and an algorithm
    the data structure is a 2D matrix, one can also think of it as a board for games #noqa
    the algorithm operates on the matrix, marking positions as visited as it goes    #noqa

    Initially, I made a class for the 2D matrix, later decided it wasn't
    necessary and in fact complicates things, for eg: it's easier to get the
    matrix dimension, len(mat), if it's just a list of lists
    - of course this could be accomplished through an instance variable as well
    but at the end of the day I didn't feel a Matrix class would buy me much.

    For this problem as well as other game-like algorithm problems
    It seems to me a good idea to think about states.
    The state of this game is captured by the
    - matrix (each cell be either 0 or 1)
    - current position, aka current cell
    - direction
    triple
    so I think about current state, next possible state, other next possible state #noqa

    For this game, after looking at the given test cases, I concluded given a
    current position, the algorithm explores the next possible step, if that's
    invalid, it could change direction and explore a different possible step,
    and if that again is invalid then the algorithm should terminate. This is
    because turning 90 degrees twice would mean going backward - not something
    a spiral would do.

    The Direction class being parent to Right, Down, Left and Up I found it
    worthwhile, it helped me being able to think about one of those directions
    at 1 time instead of all 4 in some nasty if else block
    """
    mat = [[0]*size for i in range(size)]
    mat[0][0] = 1
    go_algo = Algo(mat, (0, 0), Right())
    go_algo.run()
    return mat

class Algo(object):

    def __init__(self, mat, curr_pos, direction):
        """
        :param mat: matrix
        :param curr_pos:  a pair tuple
        :param direction: where the spiral is headed
        """
        self.mat = mat
        self.curr_pos = curr_pos
        self.direction = direction

    def run(self):
        """
        hp stands for hypothetical position
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

class Direction(object):
    @staticmethod
    def step(self, position):
        pass

    @staticmethod
    def change_direction():
        pass

class Right(Direction):
    @staticmethod
    def step(position):
        row, col = position
        return (row, col+1)

    @staticmethod
    def change_direction():
        return Down()

    def __str__(self):
        return "r"

class Down(Direction):
    @staticmethod
    def step(position):
        row, col = position
        return (row+1, col)

    @staticmethod
    def change_direction():
        return Left()

    def __str__(self):
        return "d"

class Left(Direction):
    @staticmethod
    def step(position):
        row, col = position
        return (row, col-1)

    @staticmethod
    def change_direction():
        return Up()

    def __str__(self):
        return "l"

class Up(Direction):
    @staticmethod
    def step(position):
        row, col = position
        return (row-1, col)

    @staticmethod
    def change_direction():
        return Right()

    def __str__(self):
        return "u"

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

def print_list_of_lists(ll):
    print 'matrix:'
    for row in ll:
      print row

if __name__ == '__main__':
    assert str(Right.change_direction()) == 'd'
    assert str(Down.change_direction()) == 'l'
    assert str(Left.change_direction()) == 'u'
    assert str(Up.change_direction()) == 'r'

    position = (1,1)
    assert Right.step(position) == (1,2)
    assert Down.step(position) == (2,1)
    assert Left.step(position) == (1,0)
    assert Up.step(position) == (0,1)

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
