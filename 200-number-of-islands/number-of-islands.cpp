class Solution {
    const vector<pair<int, int>>directions = {{-1,0}, {0,-1}, {1,0}, {0,1}};
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();

        if(rows == 0){
            return 0;
        }

        int cols = grid[0].size(), islands = 0;

        for(int r = 0; r<rows; r++){
            for(int c = 0; c<cols; c++){
                if(grid[r][c]=='1'){
                    islands++;
                    grid[r][c] = '0';
                    bfs(grid, r, c, rows, cols);
                }
            }
        }
        return islands;
    }

    void bfs(vector<vector<char>>& grid, int r, int c, int rows, int cols){
        queue<pair<int, int>> q;
        q.push({r, c});

        while(!q.empty()){
            pair<int, int> p = q.front();
            q.pop();
            for(int i = 0; i<4; i++){
                int dr = directions[i].first, dc = directions[i].second;
                if(p.first+dr<rows && p.second+dc<cols && p.first+dr>=0 && p.second+dc>=0 && grid[p.first+dr][p.second+dc]=='1'){
                    grid[p.first+dr][p.second+dc] = '0';
                    q.push({p.first+dr, p.second+dc});
                }
            }
        }
    }
};