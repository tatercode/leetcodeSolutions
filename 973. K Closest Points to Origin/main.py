from typing import List
import heapq
from math import sqrt
'''
Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res

        # min-heap
        # map = {}
        # dists = []
        # 
        # # O(n)
        # for point in points:
        #     x, y = point
        #     dist = sqrt((x-0)**2+(y-0)**2)
        #     if dist in map:
        #         map[dist].append(point)
        #         dists.append(dist)
        #         continue
        #
        #     map[dist] = [point]
        #     dists.append(dist)
        #
        # # Sort is O(klogn)
        # heapq.heapify(dists)
        # ans = []
        #
        # # O(k)
        # while k > 0:
        #     d = heapq.heappop(dists)
        #     for point in map[d]:
        #         ans.append(point)
        #         k-=1
        #
        # return ans 

def main():
    sol = Solution()
    ans = sol.kClosest([[1,3],[-2,2]], k = 1)
    print(ans)

    points = [[3,3],[5,-1],[-2,4]] 
    ans = sol.kClosest(points, k=2)
    print(ans)

    points = [[1, 0], [0, 1]]
    ans = sol.kClosest(points, k = 2)
    print(ans)
    return


if __name__ == "__main__":
    main()
