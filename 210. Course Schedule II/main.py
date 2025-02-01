from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        
        preMap = { i:[] for i in range(numCourses) }

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visitSet:
                return True
            
            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visitSet.add(crs)
            cycle.remove(crs)
            ans.append(crs)

            return True 

        for crs in range(numCourses):
            if not dfs(crs): return []

        return ans


if __name__ == "__main__":
    sol = Solution()
    test = [[1, 0]]
    ans = sol.findOrder(2, test)
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    ans2 = sol.findOrder(4, prerequisites)
    print(ans)
    print(ans2)

