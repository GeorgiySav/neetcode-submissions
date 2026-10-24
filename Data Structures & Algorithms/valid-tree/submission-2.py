class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[False] * n for _ in range(n)]

        for u, v in edges:
            adj[u][v] = True
            adj[v][u] = True
        
        def dfs(node, prev, visited):
            if node in visited:
                return False
            
            visited.add(node)
            for i in range(n):
                if adj[node][i] and i != prev:
                    if not dfs(i, node, visited):
                        return False
            return True
        
        visited = set()
        return dfs(0, -1, visited) and len(visited) == n