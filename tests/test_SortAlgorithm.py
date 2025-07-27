import unittest

from speciallecture.SortAlgorithm import SortAlgorithm

class TestSortAlgorithm(unittest.TestCase):

    def test_sorted_list(self):
        sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        sort = sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([-3, -1, -4, -2, -5]), [-5, -4, -3, -2, -1])

    def test_positive_random_list(self):
        sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([1, 5, 4, 2, 3]), [1, 2, 3, 4, 5])

    def test_negative_sorted_numbers(self):
        sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([-5, -4, -3, -2, -1]), [-5, -4, -3, -2, -1])

    def test_equal_list(self):
        sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([1, 2, 3, 2, 5]), [1, 2, 2, 3, 5])

    def test_pivot_equal_list(self):
        sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([4, 1, 3, 4, 2]), [1, 2, 3, 4, 4])