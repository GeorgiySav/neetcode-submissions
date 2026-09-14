class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def valid(s):
            t = 0
            for p in piles:
                t += math.ceil(p / s)
                if t > h:
                    return False
            return True

        l, r = 1, max(piles)
        res = float('inf')

        while l <= r:
            m = (l + r) // 2

            if valid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res