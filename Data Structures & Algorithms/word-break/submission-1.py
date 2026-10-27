class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = set()
        def dfs(string):
            if string in cache:
                return False
            if len(string) == 0:
                return True
            
            for w in wordDict:
                if string.startswith(w):
                    if dfs(string[len(w):]):
                        return True
            cache.add(string)
            return False
        return dfs(s)
