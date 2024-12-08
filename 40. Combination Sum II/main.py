from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int)       -> List[List[int]]:
        
        res = []

        combination = []

        def dfs(i, tot):
            if tot == target:
                combination.sort()
                if combination in res:
                    return
                res.append(combination.copy())
                return
            if i == len(candidates) or tot >= target:
                return 
            
            tot += candidates[i]
            combination.append(candidates[i])
            dfs(i + 1, tot)
            
            tot -= candidates[i]
            combination.pop()
            dfs(i + 1, tot)
            

        dfs(0, 0)

        return res

if __name__ == "__main__":
    sol = Solution()
    test = [10,1,2,7,6,1,5]
    res = sol.combinationSum2(test, 8) 
    print(res)
