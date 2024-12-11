from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_present = set()

        for n in nums:
            if n in num_present:
                return True
            num_present.add(n)

        return False

if __name__ == "__main__":
    sol = Solution()
    test = [1 ,2, 3, 4]
    test2 = [1, 2, 2, 3, 4]

    print(sol.containsDuplicate(test))
    print(sol.containsDuplicate(test2))
