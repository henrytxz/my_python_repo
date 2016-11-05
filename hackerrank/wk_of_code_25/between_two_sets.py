"""
https://www.hackerrank.com/contests/w25/challenges/between-two-sets
"""
from other_standard_problems.lcm_gcf import list_lcm, list_gcd

def btw_two_sets(A, B):
    lcm = list_lcm(A)
    gcd = list_gcd(B)
    count = 0
    # just check every int in this range, is there a cleverer way?
    # possibly but this is O(n) and good enough for the small problem size
    # specified by the question
    for x in range(lcm, gcd+1):
        if x % lcm == 0 and gcd % x == 0:
            count += 1

    return count


if __name__ == '__main__':
    A = [2,4]
    B = [16,32,96]
    assert btw_two_sets(A, B) == 3
