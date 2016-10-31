"""
Given a list_of_ints, find the highest_product you can get from three of the
integers.

We want to keep track of 2 smallest numbers
if they are both -ve, their product can be largest than the 2nd and 3rd largest
+ve numbers' product
"""
import unittest
from unittest import TestCase

def max_with_None(*args):
    return max([x for x in args if x is not None])

def min_with_None(*args):
    return min([x for x in args if x is not None])

assert max_with_None(1,2,None,-5) == 2

class Products(object):
    """
    sp stands for smallest product
    lp stands for largest product
    i denotes the product is the product of i ints
    """
    def __init__(self, sp=None, lp=None):
        self.sp = sp
        self.lp = lp

    def set_lp(self, x, product_of_1_fewer_int=None):
        if product_of_1_fewer_int is None:
            self.lp = max_with_None(self.lp, x)
        else:
            self.lp = max_with_None(self.lp, x * product_of_1_fewer_int.sp,
                                    x * product_of_1_fewer_int.lp)

    def set_sp(self, x, product_of_1_fewer_int=None):
        if product_of_1_fewer_int is None:
            self.sp = min_with_None(self.sp, x)
        else:
            self.sp = min_with_None(self.sp, x * product_of_1_fewer_int.sp,
                                    x * product_of_1_fewer_int.lp)

def init_products(A, k):
    products = []
    first_i_prods = 1
    for i in range(k):
        first_i_prods *= A[i]
        products.append(Products(first_i_prods, first_i_prods))
    return products

def get_product_of_1_fewer_int(products, num_ints):
    if num_ints == 0:
        product_num_ints_minus_1 = None
    else:
        product_num_ints_minus_1 = products[num_ints - 1]
    return product_num_ints_minus_1

def largest_product_of_k_ints(A, k):
    products = init_products(A, k)
    for x_position in range(len(A)):
        for product_index in reversed(range(k)):
            if product_index > x_position:
                continue    # not enough x to update product
            # when product_index <= x_position, there's enough x to calc a new product of that length
            product_of_1_fewer_int \
                = get_product_of_1_fewer_int(products, product_index)
            products[product_index].set_sp(A[x_position], product_of_1_fewer_int)
            products[product_index].set_lp(A[x_position], product_of_1_fewer_int)
    return products[-1].lp

def highest_product(A):
    return largest_product_of_k_ints(A, 3)


class TestHighestProduct(TestCase):
    def test_at_least_3_positive_numbers(self):
        # less than 2 -ve number
        assert highest_product([-8, 1, 2, 3, 4, 5]) == 3 * 4 * 5

        # 2 -ve numbers
        # either the 3 largest +ve numbers or
        # product or the largest +ve number * two most -ve
        assert highest_product([-8, -7, 1, 2, 3, 4, 5]) == (-8) * (-7) * 5

        # 2 - ve numbers + an 0
        assert highest_product([-10, 4, 8, 0, 12, -5]) == (-10)*12*(-5)

    def test_2_positive_numbers(self):
        # less than 2 -ve number, also A has 0
        assert highest_product([-11, 0, 4, 5]) == 0
        # A doesn't have 0
        assert highest_product([-11, -8, 4, 5]) == (-11)*(-8)*5

        # at least 2 -ve numbers
        assert highest_product([-3, -2, 0, 4, 5]) == -3*(-2)*5
        # if >= two -ve => largest * two most -ve else 0 else 3 largest

    def test_1_positive_number(self):
        # only 1 -ve number
        # has 0, no else because 1 pos 1 neg has to have 0
        assert highest_product([-11, 0, 5]) == 0
        # at least 2 -ve numbers
        self.assertEqual(highest_product([-4, -3, -2, -1, 5]), -3*(-4)*5)
        # if >= two -ve => largest * two most -ve

    def test_no_positive_number(self):
        # no 0 => multiply 3 largest numbers
        assert highest_product([-4, -3, -2, -1]) == -1*(-2)*(-3)
        # has 0 => 0
        assert highest_product([-1, -2, -3, -4, 0]) == 0

if __name__ == '__main__':
    unittest.main()
