"""
given n distinct numbers => n! permutations
the code below runs in O(n!) time and O(n!*n) space (for each permutation, it has n numbers)
"""

def insert(lst, e):
    result = []
    for i in range(len(lst)+1):
        result.append(lst[:i]+[e]+lst[i:])
    return result

def perm(A):
    if not A:
        return [[]]
    perm_n_minus_1 = perm(A[1:])
    result = []
    for p in perm_n_minus_1:
        result.extend(insert(p, A[0]))
    return result

assert perm([1,2]) == [[1,2],[2,1]]

assert len(perm([1,2,3])) == 6
assert perm([1,2,3]) == \
       [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]

assert len(perm([1,2,3,4])) == 24