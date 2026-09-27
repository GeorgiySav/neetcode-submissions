class Solution {
public:
    int area(vector<vector<int>>& grid, int x, int y) {
        if (
            x < 0 || x >= grid.size() ||
            y < 0 || y >= grid[0].size() ||
            grid[x][y] == 0
        ) return 0;

        grid[x][y] = 0; 
        return 1 + area(grid, x+1, y)
                 + area(grid, x-1, y)
                 + area(grid, x, y+1)
                 + area(grid, x, y-1);
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        int res = 0;
        for (int x = 0; x < m; ++x) {
            for (int y = 0; y < n; ++y) {
                if (grid[x][y] == 1) {
                    res = max(res, area(grid, x, y));
                }
            }
        }

        return res;
    }
};
