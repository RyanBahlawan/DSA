class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        cols = set()
        positiveDiagonal = set() #(r+c)
        negativeDiagonal = set() #(r-c)
        res = []

        board = [["."]*n for row in range(n)]

        def backtrack(r):
            #Filled each row with a queen in a valid position
            if r==n:
                copy = []
                for row in board:
                    copy.append("".join(row))
                res.append(copy)

            for c in range(n):
                #Cannot place a queen at this (r,c)
                if c in cols or (r+c) in positiveDiagonal or (r-c) in negativeDiagonal:
                    continue
                
                #We can place a queen at this (r,c)
                board[r][c] = "Q"
                cols.add(c)
                positiveDiagonal.add(r+c) #(r+c)
                negativeDiagonal.add(r-c) #(r-c)

                #Go to the next row
                backtrack(r+1)

                #Undo our changes
                board[r][c] = "."
                cols.remove(c)
                positiveDiagonal.remove(r+c) #(r+c)
                negativeDiagonal.remove(r-c) #(r-c)

        backtrack(0)
        return res