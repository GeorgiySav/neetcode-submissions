class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        l = 0
        res = 1
        table = defaultdict(int)
        maj = s[0]
        table[s[0]] = 1
        for r in range(1, len(s)):
            table[s[r]] += 1
            if table[s[r]] > table[maj]:
                maj = s[r]
            
            if table[maj] + k < r - l + 1:
                table[s[l]] -= 1
                l += 1
            else:
                res = max(res, r - l + 1)                

        return res