"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(size, r, c):
            isSame = True
            for row in range(size):
                for col in range(size):
                    if grid[r][c] != grid[r+row][c+col]:
                        isSame = False
                        break

            if isSame:
                return Node(grid[r][c], True)
            else:
                n = size//2
                topLeft = dfs(n, r, c)
                topRight = dfs(n, r, c+n)
                bottomLeft = dfs(n, r+n, c)
                bottomRight = dfs(n, r+n, c+n)
                return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)


        return dfs(len(grid), 0, 0)