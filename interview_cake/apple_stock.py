import unittest
from unittest import TestCase

def get_max_profit(stock_prices_yesterday):
    if len(stock_prices_yesterday) < 2:
        raise ValueError('cant compute a best profit with less than 2 prices')
    minimum = stock_prices_yesterday[0]
    best_profit = None
    for price in stock_prices_yesterday[1:]:
        x = price - minimum
        if not best_profit or x > best_profit:
            best_profit = x
        if price < minimum:
            minimum = price
    return best_profit


class TestGetMaxProfit(TestCase):
    def test_normal_input(self):
        self.assertEquals(get_max_profit([10, 7, 5, 8, 11, 9]), 6)

    def test_descending_all_day(self):
        self.assertEquals(get_max_profit([10, 9, 8]), -1)

    def test_edge_case(self):
        self.assertRaises(ValueError, get_max_profit, [5])


if __name__ == '__main__':
    unittest.main()