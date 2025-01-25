import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        print(stones)

        while len(stones) > 1:
            check = heapq.heappop(stones)
            check2 = heapq.heappop(stones)
            
            if check2 > check:
                heapq.heappush(stones, check-check2)
            
            

        if len(stones) == 1:
            return abs(stones[0])
        return 0


if __name__ == "__main__":
    sol = Solution()
    ans = sol.lastStoneWeight([2,7,4,1,8,1])
    print(ans)
