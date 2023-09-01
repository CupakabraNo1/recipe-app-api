"""
Sample test
"""

from django.test import SimpleTestCase

from . import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract(self):
        """Test subtracting numbers"""
        res = calc.subtract(1, 2)
        self.assertEqual(res, 1)
