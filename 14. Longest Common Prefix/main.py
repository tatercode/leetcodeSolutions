from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = "" 
        strs.sort()
        print(strs)
        first=strs[0]
        last=strs[-1]

        for i in range(min(len(first), len(last))):
            if(first[i]!=last[i]):
                return prefix 
            prefix+=first[i]

        return prefix

if __name__ == "__main__":
    sol = Solution()
    strs = ["flower","flow","flight"]
    res = sol.longestCommonPrefix(strs)
    print(res)
