#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_all_equal(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -1]), -1)

    def test_mix_positive_negative(self):
        self.assertEqual(max_integer([-10, 0, 5, -1]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.1]), 3.1)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "z", "c"]), "z")

    def test_string_list(self):
        self.assertEqual(max_integer("holberton"), "t")

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_list_with_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

if __name__ == "__main__":
    unittest.main()
