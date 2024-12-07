from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int):
        if not root:
            return -1
        if k == 0:
            return root.val

        self.kthSmallest(root.left, k - 1)
        self.kthSmallest(root.right, k - 1)


def inOrder(root):
    if not root:
        return

    inOrder(root.left)
    print(root.val)
    inOrder(root.right)


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)
    inOrder(root)
    res = sol.kthSmallest(root, 1)
    print("ans", res)
