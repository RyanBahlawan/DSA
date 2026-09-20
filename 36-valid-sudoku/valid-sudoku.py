class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        size = len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(size):
            for c in range(size):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3,c//3)].add(board[r][c])
        return True