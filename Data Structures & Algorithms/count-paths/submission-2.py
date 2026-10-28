class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            n, m = m, n

        temp = 1
        for i in range(2, n):
            temp *= i
        nf = temp

        for i in range(n, m):
            temp *= i
        mf = temp

        for i in range(m, m+n-1):
            temp *= i
        nmf = temp

        return nmf // (nf * mf)