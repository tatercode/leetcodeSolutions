from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    ans = []
    permutation = []
    def backtrack(i):
        if i == len(nums):
            ans.append(permutation.copy())
            return

        for num in nums:
            if num in permutation:
                continue 
            permutation.append(num)
            backtrack(i+1)
            permutation.pop()

    backtrack(0)
        
    return ans

if __name__ == "__main__":
    nums = [1, 2, 3]

    ans = permute(nums)
    print(ans)

