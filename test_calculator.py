# https://github.com/mjHushpuppy/Lab11-MH
# Partner 1: Michael Hushebeck
# Partner 2: Michael Hushebeck

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2 Tests
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)
        self.assertEqual(subtract(-2, -2), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, -10)
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(3, 9), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 8)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    # Partner 1 Tests
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(2, 10), 5.0)
        self.assertAlmostEqual(div(4, 2), 0.5)
        self.assertAlmostEqual(div(-2, 8), -4.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)
        with self.assertRaises(ValueError):
            logarithm(2, -5)
        with self.assertRaises(ValueError):
            logarithm(10, -1)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-4)

if __name__ == "__main__":
    unittest.main()