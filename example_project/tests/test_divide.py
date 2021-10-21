import unittest

from source.divisions.divide import divide


class TestDivide(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        dividend = 6
        divisor = 2
        result = divide(dividend, divisor)
        self.assertEqual(result, 3)

        """"
        Division by 0
        """
        dividend = 6
        divisor = 0
        result = divide(dividend, divisor)
        self.assertEqual(result, None)

        """"
        Arguments testing
        """
        dividend = None
        divisor = 0
        result = divide(dividend, divisor)
        self.assertEqual(result, None)

        """"
               Division by None
        """
        dividend = 8
        divisor = None
        result = divide(dividend, divisor)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()