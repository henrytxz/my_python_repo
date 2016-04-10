from itertools import permutations
import time

def my_generator(s):
    """
    make it into a generator to save space
    """
    ps = permutations(s)
    for p in ps:
        yield ''.join(p)

def listPosition(s):
    sorted_s = ''.join(sorted(s))
    gen = my_generator(sorted_s)
    set_values = set()
    c = 1
    for x in gen:
        set_values.add(x)
        if x == s: return len(set_values)
        c+=1

def print_unique_permutations(s):
    sorted_s = ''.join(sorted(s))
    gen = my_generator(sorted_s)
    set_values = set()
    for x in gen:
        print x
    #     set_values.add(x)
    # for s in list(set_values):
    #     print s

class Validate(object):
  @staticmethod
  def assert_equals(x, y, msg):
      if x!=y:
        print msg
        print 'actual value: {0}'.format(x)
        print 'expected value: {0}'.format(y)

if __name__ == '__main__':
    # testValues = {'A' : 1, 'ABAB' : 2, 'AAAB' : 1, 'BAAA' : 4, 'QUESTION' : 24572, 'BOOKKEEPER' : 10743}
    testValues = {'BOOKKEEPER' : 10743}
    for word in testValues:
        start = time.time()
        p = listPosition(word)
        print 'that took {0}'.format(time.time()-start)
        Validate.assert_equals(p, testValues[word], 'WRONG for: ' + word)

    # print_unique_permutations('ABAB')


