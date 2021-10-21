import unittest

from source.sums import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

        """
         Test null values
        """
        data = [1, 2, None]
        result = None
        self.assertEqual(result, None)



if __name__ == '__main__':
    unittest.main()