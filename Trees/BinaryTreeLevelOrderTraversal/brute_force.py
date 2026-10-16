# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ! See Question

# ? Question: Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

# breadth first search - Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])

        res = []

        while q:

            level_values = []
            for _ in range(len(q)):
                node = q.popleft()
                level_values.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level_values)

        return res
