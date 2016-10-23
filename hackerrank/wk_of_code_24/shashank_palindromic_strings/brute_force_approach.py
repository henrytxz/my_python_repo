from subseqs import Subseqs
from itertools import product
from time import time
from core.decorators.timer import timed_call
import cProfile

palindrome_cache = set()
not_palindrome_cache = set()

def is_palindrome(string):
    if string in palindrome_cache:
        return True
    if string in not_palindrome_cache:
        return False
    if len(string)<=1:
        return True
    if string[0] == string[-1]:
        verdict = is_palindrome(string[1:-1])
        if verdict:
            palindrome_cache.add(string)
        return verdict
    else:
        not_palindrome_cache.add(string)
        return False
    # i = 0
    # j = len(string)-1
    # while i<j:
    #     if string[i]!=string[j]:
    #         return False
    #     i+=1
    #     j-=1
    # return True


def count_palindromes(strings):
    n = len(strings)
    count = 0
    subseqs_callable_object = Subseqs()
    subseqs = subseqs_callable_object(''.join(strings))
    for x in subseqs:
        if is_palindrome(x) and len(x)>=n:
            # print x
            count += 1
    return count

@timed_call
def performance_test():
    lst = ['abc'] * 7
    lst.insert(0, 'a')
    lst.append('z')
    print count_palindromes(lst)
    # beg = time()
    # for _ in range(1000):
    #     count_palindromes(['abc', 'abc'])
    # print 'took {}'.format(time()-beg)


def tests():
    string = 'ab'
    assert string[1:-1] == ''

    assert count_palindromes(['ab', 'ab']) == 4     # aa, bb, aba, bab => 4
    assert count_palindromes(['aa', 'b', 'aa']) == 5
    assert count_palindromes(['a', 'b', 'c']) == 0
    assert count_palindromes(['abc', 'abc']) == 9
    # performance_test()


if __name__ == '__main__':
    tests()
    # cProfile.run('performance_test()')
    # performance_test()