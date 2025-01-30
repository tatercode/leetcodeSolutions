from typing import List
import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # O(n * m)
        count = Counter(tasks) # Built in hashmap counter
        maxHeap = [ -cnt for cnt in count.values() ]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time




def main():
    tasks = ["A","A","A","B","B","B"]
    n = 2

    sol = Solution()
    ans = sol.leastInterval(tasks, n)
    print(ans)
    return

if __name__ == "__main__":

    main()
