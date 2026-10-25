# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:
        def dfs(node, target):
            if not node:
                return node

            node.left = dfs(node.left, target)
            node.right = dfs(node.right, target)
            if not node.left and not node.right and node.val == target:
                return None
            else:
                return node

        return dfs(root, target)