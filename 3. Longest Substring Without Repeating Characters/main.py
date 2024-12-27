class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l, res = 0, 0
        letters = set()

        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])  # Shrink the window from the left
                l += 1
            letters.add(s[r])
            res = max(res, r - l + 1)  # Update the max length

        return res

if __name__ == "__main__":
    sol = Solution()

    test = "abcabcbb"

    res = sol.lengthOfLongestSubstring(test)

    print(res)

