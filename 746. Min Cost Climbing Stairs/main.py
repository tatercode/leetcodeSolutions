from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Brute force
        def dfs(i):

            if i >= len(cost):
                return 0

            return cost[i] + min(dfs(i+1), dfs(i+2))


        return min(dfs(0), dfs(1)) 

    # With memoization
    def minCostMemo(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]


        
        return min(dfs(0), dfs(1))
    # DP bottom up 
    def minCostDP(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n+1):
            dp[i] = min(dp[i - 1] + cost[i - 1], 
                        dp[i - 2] + cost[i - 2])
        return dp[n]

    # Optimized
    def minCostOptimized(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, - 1):
            cost[i] = min(cost[i] + cost[i + 1],
                          cost[i] + cost[i + 2])


        return min(cost[0], cost[1]) 

def main():
    cost = [1,100,1,1,1,100,1,1,100,1]
    sol = Solution()
    ans = sol.minCostClimbingStairs(cost)
    print(ans)
    ans = sol.minCostOptimized(cost)
    print(ans)

if __name__ == "__main__":
    main()
