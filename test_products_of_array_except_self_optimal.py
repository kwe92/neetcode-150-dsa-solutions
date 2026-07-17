import unittest

from ProductsofArrayExceptSelf.products_of_array_except_self import productExceptSelf


class ProductExceptSelfTests(unittest.TestCase):
    def test_simple_example(self) -> None:
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]

        self.assertEqual(productExceptSelf(nums), expected)


if __name__ == "__main__":
    unittest.main()
