from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        getAns = []
        print(nums)       
        for n in nums:
            heapq.heappush(getAns, n)
            if len(getAns) > k:
                heapq.heappop(getAns)

        return heapq.heappop(getAns)
        
    def findKthLargestQuickSelect(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(l, r) -> int:
            # Pivot chosen to be last element in sub array
            pivot, p = nums[r], l       
            # Partition
            for i in range(l, r):
                if nums[i] <= pivot:
                    # swap
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # Place pivot in correction position
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k:
                # If pivot index greater than k, search left sub
                return quickSelect(l, p - 1)
            elif p < k:
                # If pivot index less, search right subarray
                return quickSelect(p+1, r)
            else:
                # If pivot index == k return kth element
                return nums[p]

        return quickSelect(0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,1,5,6,4]
    ans = sol.findKthLargestQuickSelect(nums, 5)
    print(ans)

