from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root) -> int:
            nonlocal res 
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, left + right)

            return 1 + max(left, right)

        
        dfs(root)
        return res 

        



if __name__ == "__main__":
    root = TreeNode(1)
    temp = TreeNode(2)
    root.left = TreeNode(2)
    temp2 = TreeNode(3)
    temp.left = temp2
    temp.right = TreeNode(4)
    temp2.left = TreeNode(5)
    
    sol = Solution()
    print(sol.diameterOfBinaryTree(root))



