# Given root of binary tree invert tree and return root
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inverse(root):
            if not root:
                return
            temp = root.left
            root.left = root.right
            root.right = temp
            inverse(root.left)
            inverse(root.right)

        inverse(root)
        return root


def printBinaryTree(root: Optional[TreeNode]):
    if not root:
        return

    printBinaryTree(root.left)
    print(root.val)
    printBinaryTree(root.right)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(30)
    printBinaryTree(root)
    res = sol.invertTree(root)
    printBinaryTree(res)
