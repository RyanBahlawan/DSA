# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            nL = dfs(node.left)
            nR = dfs(node.right)

            self.res = max(self.res, nL+nR) #updates the diameter
            return 1 + max(nL,nR) #Gives us the height
        
        if not root:
            return 0

        self.res = 0
        dfs(root)
        return self.res