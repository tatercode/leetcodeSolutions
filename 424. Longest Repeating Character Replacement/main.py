class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        l = 0
        maxF = 0
        
        for r in range(len(s)):
            # count how many times letter appears
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            
            # greater than k than max replacements used shrink window
            while (r-l+1) - maxF > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)


        return res



if __name__ == "__main__":
    s = "ABBB"
    k = 1 

    sol = Solution()

    res = sol.characterReplacement(s, k)

    print(res)

