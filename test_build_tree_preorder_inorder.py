import unittest
from collections import deque
from typing import List, Optional
from Trees.ConstructBinaryTreeFromPreorderAndInorderTraversal.optimal import Solution

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_binary_tree(arr: list) -> Optional[TreeNode]:
    """Helper function to build a binary tree from a level-order array."""
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        current = queue.popleft()

        # Assign left child
        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1

        # Assign right child
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1

    return root


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Helper function to check if two binary trees are identical in structure and values."""
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


class BuildTreeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_standard_tree(self) -> None:
        # Example 1:
        # Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
        # Expected Output Tree: [3, 9, 20, None, None, 15, 7]
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expected_tree = build_binary_tree([3, 9, 20, None, None, 15, 7])

        actual_tree = self.solution.buildTree(preorder, inorder)
        self.assertTrue(is_same_tree(actual_tree, expected_tree))

    # def test_single_node(self) -> None:
    #     # Example 2:
    #     # Input: preorder = [-1], inorder = [-1]
    #     # Expected Output Tree: [-1]
    #     preorder = [-1]
    #     inorder = [-1]
    #     expected_tree = build_binary_tree([-1])

    #     actual_tree = self.solution.buildTree(preorder, inorder)
    #     self.assertTrue(is_same_tree(actual_tree, expected_tree))

    # def test_empty_input(self) -> None:
    #     # Edge Case:
    #     # Input: preorder = [], inorder = []
    #     # Expected Output: None
    #     actual_tree = self.solution.buildTree([], [])
    #     self.assertIsNone(actual_tree)


if __name__ == "__main__":
    unittest.main()
