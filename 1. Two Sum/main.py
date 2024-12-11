from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            if n not in map:
                difference = target - n
                map[difference] = i 
            else:
                return [i, map[n]]

        return [] 

if __name__ == "__main__":
    sol = Solution()
    nums = [2,7,11,15]
    t = 9
    print(sol.twoSum(nums, t))

