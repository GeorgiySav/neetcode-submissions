class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        queue<pair<int, int>> q;
        for (int x = 0; x < m; ++x) {
            for (int y = 0; y < n; ++y) {
                if (grid[x][y] == 2) q.push({x, y});
            }
        }

        int rounds = -1;
        while (!q.empty()) {
            int round_len = q.size();
            rounds += 1;

            for (int z = 0; z < round_len; ++z) {
                pair<int, int> coords = q.front(); q.pop();
                int x = coords.first;
                int y = coords.second;

                for (const auto& dir : directions) {
                    int i = x + dir[0];
                    int j = y + dir[1];

                    if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != 1) continue;
                    grid[i][j] = 2;
                    q.push({i, j});
                }
            }
        }

        for (int x = 0; x < m; ++x) {
            for (int y = 0; y < n; ++y) {
                if (grid[x][y] == 1) return -1;
            }
        }
        return max(rounds, 0);
    }

    static constexpr array<array<int, 2>, 4> directions = {{
        {1, 0}, {-1, 0}, {0, 1}, {0, -1}
    }};
};
