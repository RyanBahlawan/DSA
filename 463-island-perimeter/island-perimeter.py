class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [[-1,0], [0,1], [1,0], [0,-1]]

        def dfs(row,col):
            perimeter = 0
            #land
            if 0<=row<self.rows and 0<=col<self.cols and grid[row][col] == 1:
                grid[row][col] = 2 #mark as visited
                for (dr,dc) in self.directions:
                    nr = row+dr
                    nc = col+dc
                    perimeter+=dfs(nr,nc)
                return perimeter
            #already visited
            elif 0<=row<self.rows and 0<=col<self.cols and grid[row][col] == 2:
                return 0
            #water or out of bounds
            else:
                return 1

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 1:
                    return dfs(r,c) #since we know there is only 1 island