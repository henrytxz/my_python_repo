"""
Given a list_of_ints, find the highest_product you can get from three of the
integers.
"""
from unittest import TestCase
from heap import FixedSizeMinHeap, FixedSizeMaxHeap


def highest_product(A):
    three_largest = FixedSizeMinHeap(3)
    two_smallest = FixedSizeMaxHeap(2)
    # has_zero = False
    neg_numbers = 0
    pos_numbers = 0
    for x in A:
        three_largest.push(x)
        two_smallest.push(x)
        if x < 0:
            neg_numbers += 1
        elif x == 0:
            has_zero = True
        else:
            pos_numbers += 1

    # if pos_numbers >= 3:
    third_largest = three_largest.pop()
    second_largest = three_largest.pop()
    largest = three_largest.pop()
    return max(two_smallest.pop()*two_smallest.pop()*largest,
                 third_largest*second_largest*largest)
    # elif pos_numbers == 2:
    #     if has_zero:
    #         if neg_numbers < 2:
    #             return 0
    #         else:
    #             return max(two_smallest.pop()*two_smallest.pop(),
    #                        third_largest*second_largest) * largest
    #     else:

class TestHighestProduct(TestCase):
    def test_at_least_3_positive_numbers(self):
        # less than 2 -ve number
        assert highest_product([-8, 1, 2, 3, 4, 5]) == 3 * 4 * 5
        # at least 2 -ve numbers
        assert highest_product([-8, -7, 1, 2, 3, 4, 5]) == (-8) * (-7) * 5
        # either the 3 largest => product or the largest * two most -ve

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

"""
let's summarize:
I want to keep track of 2 smallest numbers (if they are both -ve, can be useful)
"""
