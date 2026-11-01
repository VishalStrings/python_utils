"""Unit tests for the basic calculator in app.py."""

import unittest

from app import add, divide, multiply, subtract


class TestCalculator(unittest.TestCase):
    """Tests for the four calculator operations."""

    def test_add(self) -> None:
        """add returns the sum of two numbers."""
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self) -> None:
        """subtract returns the difference of two numbers."""
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self) -> None:
        """multiply returns the product of two numbers."""
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self) -> None:
        """divide returns the quotient of two numbers."""
        self.assertEqual(divide(10, 5), 2)

    def test_divide_by_zero_raises(self) -> None:
        """divide raises ValueError when the divisor is zero."""
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
