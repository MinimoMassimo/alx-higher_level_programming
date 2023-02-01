#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class to test python file '6-max_integer'
    """
    def test_max_int_basic(self):
        """tests normal list of ints
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_int_empty(self):
        """tests if list is empty
        """
        self.assertEqual(max_integer([]), None)

    def test_max_int_neg(self):
        """tests if list has a negative int
        """
        self.assertEqual(max_integer([-1, -5, -9]), -1)

    def test_max_int_one(self):
        """tests if list has only one element
        """
        self.assertEqual(max_integer([9]), 9)
    def test_max_int_mid(self):
        """tests if max is in the middle
        """
        self.assertEqual(max_integer([0, 1, 4, -5, -9), 4)

    if __name__ == '__main__':
        unittest.main()
