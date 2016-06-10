# http://stackoverflow.com/questions/70528/why-are-pythons-private-methods-not-actually-private

import unittest

class SomeClass(object):

    def public_method(self):
        return 'public'

    def __private_method(self):
        return 'this is private!!!'

class TestPrivateAccess(unittest.TestCase):
    def test(self):
        a_class = SomeClass()
        assert a_class.public_method() == 'public'
        # a_class.__private_method()   throws an AttributeError
        assert '_SomeClass__private_method' in dir(a_class)
        ######################################################################
        assert a_class._SomeClass__private_method() == 'this is private!!!'
        ######################################################################
        """
        THE MAIN REASON FOR THE ABOVE AND FOR EVERYTHING TO BE DISCOVERABLE
        IN PYTHON IS FOR DEBUGGING CONVENIENCE

        WHEN DEBUGGING U OFTEN NEED TO "BREAK THRU THE ABSTRACTIONS"

        I.E. NOW U CAN TEST PRIVATE METHODS EASILY
        """

class Foo(object):
    def __init__(self):
        self.__baz = 42

    def foo(self):
        return self.__baz

class Bar(Foo):
    def __init__(self):
        super(Bar, self).__init__()
        self.__baz = 21

    def bar(self):
        return self.__baz

x = Bar()
assert x.foo() == 42
# this makes sense? foo is a method of the Foo class, it's fair that it doesn't
# know anything about Bar

assert x.bar() == 21
# this is also fair - the bar method belongs to the Bar class and it knows
# Bar's instance's __baz

assert x.__dict__ == {'_Bar__baz': 21, '_Foo__baz': 42}

if __name__ == '__main__':
    unittest.main()