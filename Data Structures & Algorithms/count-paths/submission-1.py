class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(i):
            res = 1
            for i in range(2, i+1):
                res *= i
            return res

        m -= 1
        n -= 1
        return factorial(m+n) // (factorial(m) * factorial(n))