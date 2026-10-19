class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions= [(-1,0),(0,1),(1,0),(0,-1)] #N,E,S,W
        res = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = "0"
            while q:
                length = len(q)
                for i in range(length):
                    row,col = q.popleft()
                    for (dr,dc) in self.directions:
                        if 0<=row+dr<self.rows and 0<=col+dc<self.cols and grid[row+dr][col+dc]=="1":
                            q.append((row+dr,col+dc))
                            grid[row+dr][col+dc] = "0"
            return

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c]=="1":
                    bfs(r,c)
                    res+=1

        return res