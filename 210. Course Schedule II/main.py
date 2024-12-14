from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        
        preMap = { i:[] for i in range(numCourses) }

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            print(crs)
            pass

        
        for crs in preMap.keys():
            dfs(crs)

        return ans


if __name__ == "__main__":
    sol = Solution()
    test = [[1, 0]]
    ans = sol.findOrder(2, test)
    print(ans)
