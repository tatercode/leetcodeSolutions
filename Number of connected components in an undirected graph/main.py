# Number of Connected Components in an Undirected Graph
# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.
#
# The nodes are numbered from 0 to n - 1.
#
# Return the total number of connected components in that graph.
#
# Example 1:
#
# Input:
# n=3
# edges=[[0,1], [0,2]]
#
# Output:
# 1
# Example 2:
#
# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]
#
# Output:
# 2
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = 0
        adjList = {i: [] for i in range(n)}

        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        visitSet = set()

        def dfs(i):
            
            if adjList == []:
                return
            
            visitSet.add(i)
            for j in adjList[i]:
                dfs(j)
            adjList[i] = []
            print(i)
            return
        
        for i in range(n):
            if i not in visitSet:
                print("Not in visitSet: ", i)
                dfs(i)
                connections += 1

        return connections 

if __name__ == "__main__":
    sol = Solution()
    ans = sol.countComponents(6, [[0,1], [1,2], [2,3], [4,5]])
    print("Solution:", ans)
    ans = sol.countComponents(3, [[0,1], [1,2]])
    print("solution:", ans)


