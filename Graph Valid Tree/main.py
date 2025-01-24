# Graph Valid Tree
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
#
# Example 1:
#
# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
#
# Output:
# true
#
# Example 2:
#
# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
#
# Output:
# false
#
# Note:
#
#     You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree can't have a cycle and a node needs to be connected

        map = {i : [] for i in range(n)}

        for parent, child in edges:
            map[parent].append(child)
            map[child].append(parent)

        # This checks to if any cycles are present
        visitSet = set()      
        def dfs(node, prev): 
            if node in visitSet: 
                return False 
            visitSet.add(node)

            for i in map[node]:
                if prev == i:
                    continue
                if not dfs(i, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visitSet) == n 

if __name__ == "__main__":
    sol = Solution()
    ans = sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]);
    print(ans)
    test = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(sol.validTree(5, test))

