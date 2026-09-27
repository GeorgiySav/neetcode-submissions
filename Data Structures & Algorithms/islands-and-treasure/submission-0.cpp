class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        queue<vector<int>> q; 

        for (int x = 0; x < m; ++x) {
            for (int y = 0; y < n; ++y) {
                if (grid[x][y] == 0) q.push({x, y});
            }
        }

        while (!q.empty()) {
            vector<int> coords = q.front(); q.pop();
            int val = grid[coords[0]][coords[1]];

            for (vector<int>& dir : vector<vector<int>>{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}) {
                vector<int> new_coords = {coords[0] + dir[0], coords[1] + dir[1]};
                if (new_coords[0] < 0 || new_coords[0] >= m ||
                    new_coords[1] < 0 || new_coords[1] >= n ||
                    grid[new_coords[0]][new_coords[1]] != 2147483647) continue;
                
                grid[new_coords[0]][new_coords[1]] = val+1;
                q.push(new_coords);
            }
        }
    }
};
