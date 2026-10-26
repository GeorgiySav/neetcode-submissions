class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0

        n = len(cost)
        dp = [0] * n

        dp[0] = cost[0]
        if len(cost) > 1:
            dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[-1], dp[-2])