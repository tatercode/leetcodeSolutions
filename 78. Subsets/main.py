from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        def dfs(i: int):
            if i == len(nums):
                ans.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            dfs(i+1)

        dfs(0)
        return ans


if __name__ == "__main__":
    test = [1, 2, 3]

    sol = Solution()

    ans = sol.subsets(test)
    print(ans)
