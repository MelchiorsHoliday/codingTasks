import unittest
import sum_recursion


class TestRecursion(unittest.TestCase):
    """
    A test case for the sum_to function in the sum_recursion module.

    This test case covers various scenarios including valid inputs,
    calculations involving floats, and error handling.

    Test Cases:
        - test_sum: Test cases for calculating the sum of elements in a list.
        - test_infinite: Test cases for calculating the sum involving floats.
        - test_errors: Test cases for handling errors such as IndexError
          and TypeError.
    """

    def test_sum(self):
        """
        Test cases for calculating the sum of elements in a list.

        Test cases here verify the correctness of the sum_to function
        when given lists of integers, including positive and negative values.
        """
        self.assertEqual(sum_recursion.sum_to([1, 2, 3, 4, 5], 4), 15)
        self.assertEqual(sum_recursion.sum_to([1, 2, 3, 4, 5], 2), 6)
        self.assertEqual(sum_recursion.sum_to([-1, 2, -3, 4, -5], 4), -3)

    def test_infinite(self):
        """
        Test cases for calculating the sum involving floats.

        """
        self.assertEqual(sum_recursion.sum_to([(10/3), 1], 1),
                         4.333333333333334)

    def test_errors(self):
        """
        Test cases for handling errors.

        """
        with self.assertRaises(IndexError):
            sum_recursion.sum_to([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 25)
        with self.assertRaises(TypeError):
            sum_recursion.sum_to(['a', 1, 2, 3, 4], 4)
        with self.assertRaises(TypeError):
            sum_recursion.sum_to([0, 1, 2, 3], 0.4)


if __name__ == '__main__':
    unittest.main()
