class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        prevprev = 1
        prev = 2

        for _ in range(2, n):
            cur = prev + prevprev
            prevprev = prev
            prev = cur
        
        return prev