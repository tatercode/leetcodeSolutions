from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if (matrix[i][len(matrix)-1] >= target and matrix[i][0] <= target):
                l, r = 0, len(matrix[i]) - 1 
                while l <= r:
                    mid = (l + r) // 2
                    print(matrix[i][mid])
                    if matrix[i][mid] == target:
                        return True
                    elif (matrix[i][mid] < target):
                        l = mid + 1
                    else:
                        r = mid - 1


        return False 


if __name__ == '__main__':
    sol = Solution()
    matrix, target = [[1,2,4,8],[10,11,12,13],[14,15,30,40]], 15
    # Should return true
    print(sol.searchMatrix(matrix, target))

    
    matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target=10

    # Should return true
    print(sol.searchMatrix(matrix, target))
