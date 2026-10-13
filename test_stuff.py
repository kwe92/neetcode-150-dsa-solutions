import unittest

from BinarySearch.FindMinimumRotatedSortedArray.blind_recall import findMin


class ProductExceptSelfTests(unittest.TestCase):
    def test_simple_example(self) -> None:
        # nums = [5, 1, 2, 3, 4]
        # target = 1
        # nums = [3, 4, 5, 6, 1, 2]
        # target = 1

        # self.assertEqual(search(nums, target), 1)

        nums = [3, 4, 5, 6, 1, 2]
        # Output: 1

        self.assertEqual(findMin(nums), 1)


if __name__ == "__main__":
    unittest.main()
