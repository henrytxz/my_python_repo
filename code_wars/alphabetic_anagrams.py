from itertools import permutations

def my_generator(s):
    """
    make it into a generator to save space
    """
    ps = permutations(s)
    for p in ps:
        yield ''.join(p)

def listPosition(s):
    sorted_s = ''.join(sorted(s))
    # print 'about to listPosition({0})'.format(sorted_s)
    gen = my_generator(sorted_s)
    set_values = set()
    c = 1
    for x in gen:
        set_values.add(x)
        if x == s: return len(set_values)
        c+=1

class Validate(object):
  @staticmethod
  def assert_equals(x, y, msg):
      if x!=y:
        print msg
        print 'actual value: {0}'.format(x)
        print 'expected value: {0}'.format(y)

if __name__ == '__main__':
    # testValues = {'A' : 1, 'AAAB' : 1}  # these 2 work
    testValues = {'A' : 1, 'ABAB' : 2, 'AAAB' : 1, 'BAAA' : 4, 'QUESTION' : 24572, 'BOOKKEEPER' : 10743}
    # testValues = {'ABAB' : 2}
    for word in testValues:
        Validate.assert_equals(listPosition(word), testValues[word], 'WRONG for: ' + word)
    #     stop = 5
    #     i = 0
    #     for p in my_generator(word):
    #         if i < stop:
    #             print p
    #         i+=1

    # ps = permutations('AABB')
    # c = 0
    # for p in ps:
    #     c+=1
    #     print ''.join(p)
    # print 'count {0}'.format(c)



