class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = len(board)
        self.cols = len(board[0])
        self.directions = [[-1,0], [0,1], [1,0], [0,-1]]
        
        #marks all non surrounded elements as T
        def dfs(r,c):
            if 0<=r<self.rows and 0<=c<self.cols and board[r][c] == "O":
                board[r][c] = "T"
                for (dr,dc) in self.directions:
                    nr = r+dr
                    nc = c+dc
                    dfs(nr,nc)

        #go through the left and right boundary
        for r in range(self.rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][self.cols-1] == "O":
                dfs(r, self.cols-1)

        #go through the top and bottom boundary
        for c in range(self.cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[self.rows-1][c] == "O":
                dfs(self.rows-1, c)


        for r in range(self.rows):
            for c in range(self.cols):
                #If we find an O, we know it is surrounded
                if board[r][c] == "O":
                    board[r][c] = "X"
                #If we find a T, we know it is not surrounded
                if board[r][c] == "T":
                    board[r][c] = "O"