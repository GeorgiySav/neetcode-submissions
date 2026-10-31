class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(si, ti):
            if not ti:
                return 1

            if (si, ti) in memo:
                return memo[(si, ti)]

            total = 0 
            for i, c in enumerate(si):
                if c == ti[0]:
                    total += dfs(si[i+1:], ti[1:])
            memo[(si, ti)] = total
            return total

        return dfs(s, t)