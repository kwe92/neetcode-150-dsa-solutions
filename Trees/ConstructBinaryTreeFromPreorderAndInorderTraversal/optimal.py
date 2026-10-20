class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # value to index map of inorder to grab indices in constant time O(1)
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0  # set initial preorder array index tracker

        # recursive DFS
        def dfs(l: int, r: int):
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        return dfs(0, len(inorder) - 1)

# Why if l > r: return None Works:

    # - No Left child:
    #       mid == l implies dfs(l, l - 1) implies l > l - 1 implies None

    # - No Right child:
    #       mid == r implies dfs(r + 1, r) implies r + 1 > r implies None
