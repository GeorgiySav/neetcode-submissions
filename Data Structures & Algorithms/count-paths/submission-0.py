class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, n):
            dp[0][i] = 1
        for j in range(1, m):
            dp[j][0] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
        
        return dp[-1][-1]