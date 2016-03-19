class Direction(object):
    # directions = ['r','d','l','u']
    #
    # def __init__(self):
    #     pass
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



    # todo turn into unittest
