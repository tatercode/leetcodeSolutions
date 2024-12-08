from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(cur) -> int:
            if (not cur):
                return 0
            
            return max(1 + dfs(cur.left),  1 + dfs(cur.right))

        return dfs(root)


if __name__ == "__main__":
    head = TreeNode(3)
    head.left = TreeNode(9)
    head.right = TreeNode(20)
    head.right.left = TreeNode(15)
    head.right.right = TreeNode(7)

    sol = Solution()
    print(sol.maxDepth(head))
