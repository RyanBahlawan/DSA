class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.directions= [(-1,0),(0,1),(1,0),(0,-1)] #N,E,S,W
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = "0"

            while q:
                pr,pc = q.popleft()
                for (dr,dc) in self.directions:
                    nr, nc = pr+dr,pc+dc
                    if 0<=nr<self.rows and 0<=nc<self.cols and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        grid[nr][nc] = "0"


        islands = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1
        return islands