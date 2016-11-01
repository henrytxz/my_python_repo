"""
http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
"""

def primes(n):
    """ Returns  a list of primes < n
        this is not the fastest way but it is indepedent of other libs
    """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

if __name__ == '__main__':
    assert primes(20) == [2,3,5,7,11,13,17,19]