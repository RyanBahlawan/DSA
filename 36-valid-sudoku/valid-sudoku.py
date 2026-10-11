class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        size = len(board[0])

        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(size):
            for c in range(size):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3,c//3)]):
                    return False
                else:
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    square[(r//3, c//3)].add(board[r][c])
        return True