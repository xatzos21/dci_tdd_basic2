import unittest
from app import rnd, max_num_in_list

class TestApp(unittest.TestCase):
    # check if max_num_in_list will return right value
    def test_max_num_in_list1(self):
        self.assertEqual(max_num_in_list([2, 6, 8, 7, -1]), 8, 'return value not the greatest value in max_num_in_list')

    # this is my proper solution to define if it produces a correct value or an out of range one
    # due to the randomness of the result produced from the function
    def test_correct_value1(self):
        result = rnd(2, 20)
        self.assertGreaterEqual(result, 2)
        self.assertLessEqual(result, 20)

    # i was playing with assertIn as an answer to task2
    def test_range_of_value(self):
        result2 = rnd(2, 20)
        expected_range = [2, 3, 4, 5, 6, 7, 8, 9, 10, \
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertIn(result2, expected_range)

if __name__ == '__main__':
    unittest.main()