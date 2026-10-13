# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        arr = []

        def traversal(node):
            if not node:
                return

            traversal(node.left)
            traversal(node.right)
            arr.append(node.val)

        traversal(root)
        return arr            