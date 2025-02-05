class Solution:
    # Top-down
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0) 
    # Bottom up O(n)
    def climbStairsDP(self, n: int) -> int:
        
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    # Space optimized
    def climbStairsOptimal(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

def main():
    sol = Solution()
    ans = sol.climbStairs(5)
    print(ans)
    ans = sol.climbStairs(3)
    print(ans)

if __name__ == "__main__":
    main()
