class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        strings = []

        def dfs(s, n_open):
            if len(s) >= n*2:
                if n_open == 0:
                    strings.append(s)
                return
                
            if n_open > 0:
                dfs(s + ")", n_open-1)
            if n_open < n:
                dfs(s + "(", n_open+1)
        
        dfs("", 0)
        return strings
