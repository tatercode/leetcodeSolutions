from typing import List

class Solution:
    # Space optimized
    def rob(self, nums: List[int]) -> int: 
        rob1, rob2 = 0, 0 
        
        # Only need to keep track 
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp


        return rob2

if __name__ == "__main__":
    sol = Solution()
    
    ans = sol.rob([1, 2, 3, 1])
    print(ans)
