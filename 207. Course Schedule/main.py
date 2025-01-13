'''
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjency list
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        print(preMap)
        
        #Check if cycle
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # We know course can be completed so remove
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True

if __name__ == "__main__":
    sol = Solution()

    test = [[0, 1]]
    
    print(sol.canFinish(2, test))
    test = [[1,0],[0,1]]
    print(sol.canFinish(2, test))
