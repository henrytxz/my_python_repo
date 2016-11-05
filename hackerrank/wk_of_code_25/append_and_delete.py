"""
https://www.hackerrank.com/contests/w25/challenges/append-and-delete
"""

from verbose_assert import verbose_assert

def append_and_delete(s, t, k):
    ls = len(s)
    lt = len(t)
    num_same_chars = count_number_same_chars(ls, lt, s, t)
    if yes_reason_1(ls, lt, k) or yes_reason_2(ls, lt, k, num_same_chars):
        return 'Yes'
    else:
        return 'No'

def yes_reason_1(ls, lt, k):
    # k2 => how many characters total is it to delete all chars of s then
    # append all chars of t, if k >= k2, you can turn s into t for sure
    k2 = ls + lt
    return k >= k2

def yes_reason_2(ls, lt, k, num_same_chars):
    # k1 is the min number of deletes + min number of appends needed to turn s into t
    # => k will need to >= k1
    # if k > k1, it needs to be an even number more than k1
    # for example: hackerhappy to hackerrank, k = 11 works but k = 12 doesn't
    k1 = (max(ls, lt) - num_same_chars) + (min(ls, lt) - num_same_chars)
    return (k >= k1 and (k - k1) % 2 == 0)

def count_number_same_chars(ls, lt, s, t):
    num_same_chars = 0
    for i in range(min(ls, lt)):
        if s[i] == t[i]:
            num_same_chars += 1
        else:  # stop at the 1st different character
            break
    return num_same_chars


if __name__ == '__main__':
    verbose_assert('Yes', append_and_delete('hackerhappy', 'hackerrank', 9))
    verbose_assert('Yes', append_and_delete('hackerhappy', 'hackerrank', 11))
    verbose_assert('Yes', append_and_delete('hackerhappy', 'hackerrank', 13))

    verbose_assert('Yes', append_and_delete('aba', 'aba', 7))
    verbose_assert('Yes', append_and_delete('aba', 'aba', 6))
    verbose_assert('No', append_and_delete('aba', 'aba', 5))
    verbose_assert('Yes', append_and_delete('aba', 'aba', 0))
    verbose_assert('Yes', append_and_delete('abc', 'add', 7))
    verbose_assert('Yes', append_and_delete('ab', 'abcdefghi', 7))