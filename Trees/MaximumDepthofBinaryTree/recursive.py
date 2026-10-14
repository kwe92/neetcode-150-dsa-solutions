from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_binary_tree(arr: list) -> Optional[TreeNode]:
    """
    Helper function to build a binary tree from a level-order array (LeetCode format).
    Use None for 'null' nodes.
    """
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


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


if __name__ == '__main__':
    # Example 1:
    # Input: root = [1, 2, 3, null, null, 4]
    # Output: 3
    root1 = build_binary_tree([1, 2, 3, None, None, 4])
    result1 = maxDepth(root1)
    print(f"Example 1 Output: {result1}")
    print("Expected Output: 3\n")

    # Example 2:
    # Input: root = []
    # Output: 0
    root2 = build_binary_tree([])
    result2 = maxDepth(root2)
    print(f"Example 2 Output: {result2}")
    print("Expected Output: 0\n")
