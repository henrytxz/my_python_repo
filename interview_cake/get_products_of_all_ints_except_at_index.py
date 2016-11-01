def get_products_of_all_ints_except_at_index(A):
    if not A or len(A)==1:
        return [1]  # product of 0 ints, think of it as x^0 => 1
    product_before_i = [A[0]]    # 1 to make product_before_i same length as A, to make things simpler
    for i in range(1, len(A)-1):
        product_before_i.append(product_before_i[i-1]*A[i])
    product_before_i.insert(0, 1)
    product_after_i = 1
    for i in range(len(A)-1, -1, -1):
        curr = A[i]
        A[i] = product_before_i[i]*product_after_i
        product_after_i *= curr
    return A


if __name__ == '__main__':
    A = [1,2,6,5,9]
    assert get_products_of_all_ints_except_at_index(A) == [540, 270, 90, 108, 60]

    A = [1,7,3,4]
    assert get_products_of_all_ints_except_at_index(A) == [84, 12, 28, 21]
