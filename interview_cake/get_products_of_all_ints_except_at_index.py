
def get_products_of_all_ints_except_at_index(A):
    if not A:
        return []
    product_from_beg = {}
    product_from_beg[0] = A[0]
    for i in range(1, len(A)-1):
        product_from_beg[i] = product_from_beg[i-1] * A[i]

    product_from_end = {}
    end = len(A) - 1
    product_from_end[end] = A[-1]
    for j in range(end-1, 0, -1):
        product_from_end[j] = product_from_end[j+1] * A[j]

    result = [None]*len(A)
    for k in range(len(A)):
        if k == 0:
            result[k] = product_from_end[k+1]
        elif k == end:
            result[k] = product_from_beg[k-1]
        else:
            result[k] = product_from_beg[k-1]*product_from_end[k+1]
    return result

A = [1,2,6,5,9]
assert get_products_of_all_ints_except_at_index(A) == [540, 270, 90, 108, 60]
