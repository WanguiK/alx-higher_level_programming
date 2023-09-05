#!/usr/bin/python3

"""
Unittest for max_integer([..])
"""


import unittest
from max_integer import max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 3, 2, 1]), 3)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 10000000, 100000000]), 100000000)

if __name__ == '__main__':
    unittest.main()
