class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = Counter(s)
        t_count = defaultdict(int)

        for c in t:
            t_count[c] += 1
            if t_count[c] > s_count[c]:
                return False

        return True