# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        # Use bfs to find right most node
        q = deque()
        q.append(root)
        res.append(root.val)
        while q:
            last_val = None
            for _ in range(len(q)):
                cur = q.popleft()
                print(cur.val)
                if cur.left:
                    q.append(cur.left)
                    last_val = cur.left.val
                if cur.right:
                    q.append(cur.right)
                    last_val = cur.right.val

            res.append(last_val)
        if res[len(res) - 1] is None:
            res.pop()
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    sol = Solution()
    res = sol.rightSideView(root)
    print(res)
