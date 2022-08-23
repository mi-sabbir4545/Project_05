import Code_Coverage.mymath as mymath
import unittest


class TestAdd(unittest.TestCase):
    """
    Test add function from mymath
    """

    def test_add_integer(self):
        """
        Test add of two integer returns to the correct total
        """
        result = mymath.add(10, 5)
        self.assertEqual(result, 15)

    def test_add_float(self):

        result = mymath.add(10.5, 5.5)
        self.assertEqual(result, 16)

    def test_add_string(self):

        result = mymath.add('flower', 'tree')
        self.assertEqual(result, 'flowertree')

    def test_subtract_string(self):

        result = mymath.subtraction(10, 5)
        self.assertEqual(result, 5)

    def test_multiply_integer(self):

        result = mymath.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide_integer(self):

        result = mymath.divide(10, 5)
        self.assertEqual(result, 2)

    def test_integer(self):

        result = mymath.divide(10, 5)
        self.assertEqual(result, 2)

    def test_integer_type(self):

        result = mymath.divide(10, 5)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
