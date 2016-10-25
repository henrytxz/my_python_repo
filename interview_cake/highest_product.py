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

    def set_lp(self, x, product_i_minus_1):
        done = self.lp is None
        if product_i_minus_1 is None:
            self.lp = max_with_None(self.lp, x)
        else:
            self.lp = max_with_None(self.lp, x * product_i_minus_1.sp,
                                    x * product_i_minus_1.lp)
        return done

    def set_sp(self, x, product_i_minus_1):
        if product_i_minus_1 is None:
            self.sp = min_with_None(self.sp, x)
        else:
            self.sp = min_with_None(self.sp, x * product_i_minus_1.sp,
                                    x * product_i_minus_1.lp)

from copy import deepcopy

def largest_product_of_k_ints(A, k):
    products = [Products() for _ in range(k)]
    for x in A:
        curr_products = deepcopy(products)
        for i in range(k):
            if i == 0:
                product_i_minus_1 = None
            else:
                product_i_minus_1 = curr_products[i-1]
            if i != k-1:
                products[i].set_sp(x, product_i_minus_1)
            done = products[i].set_lp(x, product_i_minus_1)
            if done:
                break
    return products[-1].lp

def highest_product(A):
    return largest_product_of_k_ints(A, 3)


class TestHighestProduct(TestCase):
    def test_at_least_3_positive_numbers(self):
        # less than 2 -ve number
        assert highest_product([-8, 1, 2, 3, 4, 5]) == 3 * 4 * 5

        # 2 -ve numbers
        assert highest_product([-8, -7, 1, 2, 3, 4, 5]) == (-8) * (-7) * 5
        # either the 3 largest => product or the largest * two most -ve

        # 2 - ve numbers + an 0
        assert highest_product([-10, 4, 8, 0, 12, -5]) == (-10)*12*(-5)

    def test_2_positive_numbers(self):
        # less than 2 -ve number
        # has 0
        assert highest_product([-11, 0, 4, 5]) == 0
        # doesn't have 0
        assert highest_product([-11, -8, 4, 5]) == (-11)*(-8)*5

        # at least 2 -ve numbers
        assert highest_product([-3, -2, 0, 4, 5]) == -3*(-2)*5
        # if >= two -ve => largest * two most -ve else 0 else 3 largest

    def test_1_positive_number(self):
        # only 1 -ve number
        # has 0, no else because 1 pos 1 neg has to have 0
        assert highest_product([-11, 0, 5]) == 0
        # at least 2 -ve numbers
        assert highest_product([-4, -3, -2, -1, 5]) == -3*(-4)*5
        # if >= two -ve => largest * two most -ve

    def test_no_positive_number(self):
        # no 0 => multiply 3 largest numbers
        assert highest_product([-4, -3, -2, -1]) == -1*(-2)*(-3)
        # has 0 => 0
        assert highest_product([-1, -2, -3, -4, 0]) == 0

if __name__ == '__main__':
    unittest.main()
