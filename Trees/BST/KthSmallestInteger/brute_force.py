class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        q = deque([root])
        node_vals = []

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                node_vals.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        node_vals.sort()

        return node_vals[k-1]
