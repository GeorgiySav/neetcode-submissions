class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        coins = [c for c in coins if c <= amount]
        if not coins:
            return -1

        dp = [-1] * (amount+1)
        for c in coins:
            dp[c] = 1
        
        for i in range(max(coins) + 1, amount+1):
            dp[i] = float('inf')
            for c in coins:
                if dp[i-c] != -1:
                    dp[i] = min(dp[i], dp[i-c])
            if dp[i] != float('inf'):
                dp[i] += 1
            else:
                dp[i] = -1
        
        return dp[-1]