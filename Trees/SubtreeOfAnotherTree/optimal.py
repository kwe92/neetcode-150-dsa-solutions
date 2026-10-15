# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # determine edge / base cases to exit recursion

        # 1. subroot is empty; if subroot is empty it will always be a subtree of any tree definition
        if not subRoot:
            return True

        # 2. a non-empty subRoot can not be a subtree of an empty root
        if not root:
            return False

        # 3. if the trees are equal then we are done
        if self.issameTree(root, subRoot):
            return True

        # recursively traverse the right and left subtrees of root to check if subRoot is a sub tree of the right or left branch; if either returns true then subRoot is a subtree of root
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    # we first need a way to determine if the two trees are equivalent
    def issameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        # determine edge cases to exit recursion

        # 1. both root and subRoot were initially null or we have traversed past the leaf nodes of both trees simultaneously with matching values
        if not root and not subRoot:
            return True
        # 2.  one tree is deeper than the other or their values are not equal
        if (not root or not subRoot) or (root.val != subRoot.val):
            return False

        return (self.issameTree(root.left, subRoot.left) and self.issameTree(root.right, subRoot.right))
