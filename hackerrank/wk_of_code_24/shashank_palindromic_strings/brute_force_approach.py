from subseqs import Subseqs
from itertools import product

def is_palindrome(string):
    i = 0
    j = len(string)-1
    while i<j:
        if string[i]!=string[j]:
            return False
        i+=1
        j-=1
    return True

def count_palindromes(strings):
    count = 0
    subseqs = Subseqs()
    set_subseqs = []
    for string in strings:
        set_subseqs.append(subseqs(string))

    for tuple_subseqs in product(*set_subseqs):
        if is_palindrome(''.join(tuple_subseqs)):
            count += 1

    return count


def tests():
    assert count_palindromes(['ab', 'ab']) == 4     # aa, bb, aba, bab => 4
    assert count_palindromes(['aa', 'b', 'aa']) == 5
    assert count_palindromes(['a', 'b', 'c']) == 0
    assert count_palindromes(['abc', 'abc']) == 9

if __name__ == '__main__':
    tests()
