class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        while matrix:
            #Step 1: Add the first row of the matrix
            if matrix[0]:
                res += (matrix.pop(0))
            
            #Step 2: Add the last element of each row
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            
            #Step 3: Add the reverse of the last row
            if matrix:
                res += (matrix.pop()[::-1])
            
            #Step 4: In reverse, add the first element of each row
            if matrix and matrix[-1]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res