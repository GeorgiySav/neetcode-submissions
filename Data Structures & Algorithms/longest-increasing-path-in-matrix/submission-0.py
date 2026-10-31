class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(x, y):
            if (x, y) in memo:
                return memo[(x, y)]
            
            memo[(x, y)] = 0
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            max_path = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx == m or ny < 0 or ny == n or matrix[nx][ny] <= matrix[x][y]:
                    continue
                
                max_path = max(max_path, dfs(nx, ny) + 1)
            memo[(x, y)] = max_path
            return max_path

        res = 0 
        for x in range(m):
            for y in range(n):
                res = max(res, dfs(x, y))
            
        return res