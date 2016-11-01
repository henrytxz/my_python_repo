"""
https://www.hackerrank.com/contests/w25/challenges/between-two-sets
"""
from other_standard_problems.lcm_gcf import list_lcm, list_gcd
# from at_least_partially_borrowed_from_web.primes import primes

# primes_under_100 = primes(100)

def btw_two_sets(A, B):
    lcm = list_lcm(A)
    gcd = list_gcd(B)
    count = 0
    # if gcd % lcm == 0:
    #     count += 1
    for x in range(lcm, gcd+1):
        if x % lcm == 0 and gcd % x == 0:
            # print x
            count += 1

    # for p in primes_under_100:
    #     if gcd % (lcm*p) == 0:

    return count


if __name__ == '__main__':
    A = [2,4]
    B = [16,32,96]
    print btw_two_sets(A, B)
