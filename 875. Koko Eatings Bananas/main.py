from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = float('inf')

        while l <= r:
            mid = (r+l) // 2
            time = 0
            for p in piles:
                time += math.ceil(p/mid)
            
            if time <= h:
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1

        return int(k)


def main():
    sol = Solution()
    piles = [3,6,7,11]
    h = 8
    ans = sol.minEatingSpeed(piles, h)
    print(ans)


if __name__ == "__main__":
    main()
