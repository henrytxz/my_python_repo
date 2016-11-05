def get_products_of_all_ints_except_at_index(A):
    if not A:       # or len(A)==1:
        return [1]  # product of 0 ints, think of it as x^0 => 1
    products_before_i = []
    for i in range(len(A)):
        if i==0:
            products_before_i.append(1)
        else:
            products_before_i.append(products_before_i[i-1]*A[i-1])
    product_after_index = 1
    for index in range(len(A)-1, -1, -1):
        curr_value = A[index]
        A[index] = products_before_i[index]*product_after_index
        product_after_index *= curr_value
    return A


def test_0_works():
    A = [2, 0, 4]
    assert get_products_of_all_ints_except_at_index(A) == [0, 8, 0]

def test_1_element_list_works():
    A = [3]
    assert get_products_of_all_ints_except_at_index(A) == [1]

def test_empty_list_works():
    assert get_products_of_all_ints_except_at_index([]) == [1]


if __name__ == '__main__':
    test_0_works()
    test_1_element_list_works()
    test_empty_list_works()

    A = [1,2,6,5,9]
    assert get_products_of_all_ints_except_at_index(A) == [540, 270, 90, 108, 60]

    A = [1,7,3,4]
    assert get_products_of_all_ints_except_at_index(A) == [84, 12, 28, 21]

    A = [2,3,4]
    assert get_products_of_all_ints_except_at_index(A) == [12, 8, 6]

