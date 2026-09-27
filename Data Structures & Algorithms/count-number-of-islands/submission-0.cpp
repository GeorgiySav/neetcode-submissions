class Solution {
public:
    void fill(vector<vector<char>>& grid, int x, int y) {
        if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size()) return;
        if (grid[x][y] != '1') return;
        grid[x][y] = '#';
        fill(grid, x+1, y);
        fill(grid, x-1, y);
        fill(grid, x, y+1);
        fill(grid, x, y-1);
    }
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        int res = 0;
        for (int x = 0; x < m; ++x) {
            for (int y = 0; y < n; ++y) {
                if (grid[x][y] == '1') {
                    res++;
                    fill(grid, x, y);
                }
            }
        }
        return res;
    }
};
