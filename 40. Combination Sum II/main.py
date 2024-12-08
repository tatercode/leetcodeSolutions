from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int)       -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, tot, combination):
            if tot == target:
                res.append(combination.copy())
                return

            if i == len(candidates) or tot >= target:
                return 
            
            combination.append(candidates[i])
            dfs(i + 1, tot+candidates[i], combination)
            combination.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            dfs(i+1, tot, combination)

        dfs(0, 0, [])

        return res

if __name__ == "__main__":
    sol = Solution()
    test = [2,5,2,1,2]
    res = sol.combinationSum2(test, 8) 
    print(res)
