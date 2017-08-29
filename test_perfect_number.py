import unittest
from perfect_number import is_perfect


class TestPerfectNumber(unittest.TestCase):
    def test_perfect_number(self):
        self.assertTrue(is_perfect(16))

    def test_not_perfect_number(self):
        self.assertFalse(is_perfect(7))

    def test_number_one(self):
        self.assertFalse(is_perfect(1))

    def test_number_zero(self):
        self.assertFalse(is_perfect(0))

    def test_large_number(self):
        self.assertTrue(is_perfect(33550336))


if __name__ == '__main__':
    unittest.main()
