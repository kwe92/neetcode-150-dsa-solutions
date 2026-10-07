import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent / \
    "ContainerWithMostWater" / "container_with_most_water.py"
SPEC = importlib.util.spec_from_file_location(
    "container_with_most_water", MODULE_PATH)
container_with_most_water = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(container_with_most_water)


class TestMaxArea(unittest.TestCase):
    def test_example_case(self) -> None:
        heights = [1, 7, 2, 5, 4, 7, 3, 6]
        self.assertEqual(container_with_most_water.maxArea(heights), 36)


if __name__ == "__main__":
    unittest.main()
