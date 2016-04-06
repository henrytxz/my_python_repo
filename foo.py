def f(x):
    return x+x

def g(an_object, new_value):
    an_object.value = new_value

def twice(y):
    y *=2
    print y

class myClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

if __name__ == '__main__':
    # z = 7
    # twice(z)
    # print z
    #
    # my_object = myClass(3)
    # assert my_object.get_value() == 3
    #
    # g(my_object, 5)
    # print my_object.get_value()

    # a_string = 'abc'
    # print f(a_string)
    #
    # b_string = a_string
    # a_string = 'def'
    # print b_string

    # x = 'abc'
    # y = 'def'
    # # y = 3
    # print id(x)==id(y)
    # # print id(x)
    #
    import copy
    # y = copy.deepcopy(x)
    # print id(x)==id(y)

    x = {'a':1}
    y = copy.deepcopy(x)
    print id(x)==id(y)

    x = 3
    y = copy.deepcopy(x)
    print id(x)==id(y)