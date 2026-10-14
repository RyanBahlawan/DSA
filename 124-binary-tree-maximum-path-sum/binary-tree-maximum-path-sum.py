# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.res = root.val #Stores the best possible path

        #This function returns the best extendable path
        def dfs(node):
            if not node:
                return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            self.res = max(self.res, node.val+leftMax+rightMax) #Best path
            return max(node.val+leftMax, node.val+rightMax, 0) #Best extendable path


        dfs(root)
        return self.res