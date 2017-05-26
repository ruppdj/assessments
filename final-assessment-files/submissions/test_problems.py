'''
Unit tests for the Section 1 - Python problems of the Final Assessment
To run the tests: make test
'''

import unittest as unittest
import problems as p
import numpy as np

class TestProblems(unittest.TestCase):

    def test_column_averages(self):
        result = p.column_averages('data/example.csv')
        answer = {'A': 0.35999999999999999, 'B': 1330.8, 'C': 64.200000000000003}
        # should this be assertAlmostEqual? Or, specify something more specific...?
        self.assertEqual(result, answer)


    def test_filter_by_class(self):
        X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        y = np.array(["a", "c", "a", "b"])
        result1 = p.filter_by_class(X, y, "a")
        answer1 = np.array([[1, 2, 3], [7, 8, 9]])
        result2 = p.filter_by_class(X, y, "b")
        answer2 = np.array([[10,11,12]])
        self.assertTrue(np.array_equal(result1, answer1))
        self.assertTrue(np.array_equal(result2, answer2))


    def test_etsy_query(self):
        result = p.etsy_query("data")
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
