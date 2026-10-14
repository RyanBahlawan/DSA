class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.q = deque()
        self.total = 0
        time = 0

        def bfs(r,c):
            if r>=self.rows or r<0 or c>=self.cols or c<0 or grid[r][c]==0:
                return
            self.q.append((r,c))
            self.total-=1
            grid[r][c]=0
            return
            

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c]==1:
                    self.total+=1
                if grid[r][c]==2:
                    self.q.append((r,c))
                    grid[r][c]=0

        while self.q and self.total > 0:
            for i in range(len(self.q)):
                r, c = self.q.popleft()
                bfs(r-1,c) #N
                bfs(r,c+1) #E
                bfs(r+1,c) #S
                bfs(r,c-1) #W
            time+=1

        if self.total==0:
            return time
        else:
            return -1