# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        n = 0
        curr = root

        while curr or stack:
            #Traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            #Process (curr is at NULL now)
            curr = stack.pop()
            n+=1
            if n==k:
                return curr.val

            #Traverse right
            curr = curr.right