class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.sumMatrix = [[0]*(cols+1) for i in range(rows+1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix+=matrix[r][c]
                above = self.sumMatrix[r][c+1]
                self.sumMatrix[r+1][c+1] = prefix+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1
        col1+=1
        row2+=1
        col2+=1

        topRight = self.sumMatrix[row1-1][col2]
        topLeft = self.sumMatrix[row1-1][col1-1]
        bottomRight = self.sumMatrix[row2][col2]
        bottomLeft = self.sumMatrix[row2][col1-1]

        return bottomRight - bottomLeft - topRight + topLeft



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)