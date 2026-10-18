class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        cols = len(heights[0])
        rows = len(heights)

        cells = set()

        def climb(r, c, ph, visited):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if heights[r][c] < ph:
                return
            if (r, c) in visited:
                return

            visited.add((r, c))

            directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
            for offset in directions:
                climb(r + offset[0], c + offset[1], heights[r][c], visited) 

        # pacific flood fill
        pacific_visited = set()
        for c in range(cols):
            climb(0, c, -float('inf'), pacific_visited)
        for r in range(rows):
            climb(r, 0, -float('inf'), pacific_visited)
        
        # atlantic flood fill
        atlantic_visited = set()
        for c in range(cols):
            climb(rows-1, c, -float('inf'), atlantic_visited)
        for r in range(rows):
            climb(r, cols-1, -float('inf'), atlantic_visited)
        
        return [[r, c] for r, c in (pacific_visited & atlantic_visited)]