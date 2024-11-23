from collections import deque
from typing import List

class Solution: 
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1 
        
        directions = [[0, 1], [0,-1], [1,0], [-1,0]]
        # Using BFS to start the search at the rotten fruits 
        # From the rotten fruits check every direction for fresh fruits
        # If fruit is fresh change to rotten and add to queue
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                r, c = queue.popleft() 
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row >= ROWS or col >= COLS or row < 0 or col < 0 or grid[row][col] != 1:
                       continue
                    grid[row][col] = 2
                    print("In here")
                    queue.append((row, col))
                    fresh -= 1 
            time += 1 

        return time 




if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]

    print(grid)

    sol = Solution()
    res = sol.orangesRotting(grid)
    print(res)
    print(grid)
