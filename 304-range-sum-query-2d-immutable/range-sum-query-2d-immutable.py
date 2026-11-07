class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        #at [r][c] it tells you the prefix sum of the matrix
        self.sumMatrix = [[0]*(cols+1) for i in range(rows+1)]

        #current value+above+left-topleft
        for r in range(1,rows+1):
            for c in range(1,cols+1):
                self.sumMatrix[r][c] = matrix[r-1][c-1]+self.sumMatrix[r-1][c]+self.sumMatrix[r][c-1]-self.sumMatrix[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1
        col1+=1
        row2+=1
        col2+=1
        
        #bottom right-top-left+topleft
        bottomRight = self.sumMatrix[row2][col2]
        top = self.sumMatrix[row1-1][col2]
        left = self.sumMatrix[row2][col1-1]
        topLeft = self.sumMatrix[row1-1][col1-1]
        sum = bottomRight-top-left+topLeft
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)