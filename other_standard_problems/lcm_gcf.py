"""
least common multiple
and
greatest common factor
"""

from verbose_assert import verbose_assert

# define gcd function
def gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""

   while(y):
       x, y = y, x % y

   return x

# define lcm function
def lcm(x, y):
   """This function takes two integers and returns the L.C.M."""

   lcm = (x*y)//gcd(x,y)
   return lcm

def list_lcm_or_gcd(A, func):
    if not A or len(A) == 0:
        return 1
    if len(A) == 1:
        return A[0]
    result_so_far = func(A[0], A[1])
    new_list = [result_so_far] + A[2:]
    return list_lcm_or_gcd(new_list, func)

def list_lcm(A):
    return list_lcm_or_gcd(A, lcm)

def list_gcd(A):
    return list_lcm_or_gcd(A, gcd)

if __name__ == '__main__':
    verbose_assert(1, actual=gcd(6,7))
    verbose_assert(2, actual=gcd(6,8))
    verbose_assert(6, actual=gcd(6,12))
    verbose_assert(6, actual=list_gcd([6,12]))
    verbose_assert(16, actual=list_gcd([16,32,96]))

    verbose_assert(4, actual=lcm(2,4))
    verbose_assert(12, actual=lcm(3,4))
    verbose_assert(4, actual=list_lcm([2,4]))
    verbose_assert(12, actual=list_lcm([2,4,3]))
