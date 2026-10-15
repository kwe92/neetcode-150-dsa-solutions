
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if not p and not q:
        return True

    if (not p or not q) or (q.val != p.val):
        return False

    return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))


if __name__ == '__main__':
    pass
