from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque()
        visit = set() 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visit.add((r,c))

        
        def addCell(r, c):
            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == -1):
                return
            visit.add((r,c))
            queue.append((r,c))
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    addCell(r+dr, c+dc)
            dist += 1


if __name__ == "__main__":
    sol = Solution()
    grid = [
            [2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]
            ]
    sol.wallsAndGates(grid)
    print(grid)
