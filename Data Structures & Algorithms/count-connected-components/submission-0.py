class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        unvisited = [True] * n
        def dfs(node):
            if not unvisited[node]:
                return
            
            unvisited[node] = False
            for nei in adj[node]:
                dfs(nei)

        res = 0
        for i in range(n):
            if unvisited[i]:
                res += 1
                dfs(i)
        return res