class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        size = len(board)
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(size):
            for c in range(size):
                digit = board[r][c]
                if digit == ".":
                    continue
                elif digit in row[r] or digit in col[c] or digit in square[(r//3, c//3)]:
                    return False
                else:
                    row[r].add(digit)
                    col[c].add(digit)
                    square[(r//3, c//3)].add(digit)
        return True