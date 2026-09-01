class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            h = ''.join(sorted(s))
            if h in groups:
                groups[h].append(s)
            else:
                groups[h] = [s]
        
        return [v for v in groups.values()]