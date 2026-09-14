class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        dp = [0] * len(s)
        dp[0] = 1

        for i in range(1, len(s)):
            c = s[i]
            if (int(s[i-1]) == 2 and int(c) < 7) or int(s[i-1]) == 1:
                if i > 2:
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 1
            if c != '0':
                dp[i] += dp[i-1]

        return dp[-1]