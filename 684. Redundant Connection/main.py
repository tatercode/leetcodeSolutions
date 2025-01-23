from typing import List


class Solution:
    # Union Find Time O(V+E(alpha * (V))) Space: O(V)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        
        return []

    def findRedundantDFS(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        # Build adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [False] * (n + 1)
        cycle = set()
        cycleStart = -1

        # DFS to detect the cycle
        def dfs(node, parent):
            nonlocal cycleStart
            visit[node] = True

            for nei in adj[node]:
                if nei == parent:
                    continue  # Skip the parent node

                if visit[nei]:  # Cycle detected
                    cycleStart = nei
                    cycle.add(node)
                    return True

                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:  # End of cycle
                        cycleStart = -1
                        return True
                    return True

            return False

        # Start DFS from node 1
        dfs(1, -1)

        # Find the last edge in the cycle
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []



if __name__ == "__main__":
    sol = Solution()
    ans = sol.findRedundantConnection([[1,2],[1,3],[2,3]])
    print(ans) 
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    print(sol.findRedundantConnection(edges))
