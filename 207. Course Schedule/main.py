from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = { i:[] for i in range(numCourses) }

        print(preMap)
    
        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        def dfs(crs):
            # Detected loop
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True

if __name__ == "__main__":
    sol = Solution()

    test = [[0, 1]]

    print(sol.canFinish(2, test))
