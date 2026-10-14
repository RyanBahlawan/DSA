# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        #We are iterating through preorder by doing recursion
        #we are using a hashmap to get the index of the middle  since we know everything to the left of the middle is on the left subtree and everything to the right is on the right subtree
        self.pre_index = 0
        roots = {val:idx for idx,val in enumerate(inorder)}

        def dfs(l,r):
            if l>r:#reached a NULL
                return None

            rootVal = preorder[self.pre_index]
            mid = roots[rootVal] #This allows us to search for the mid in O(1)
            root = TreeNode(rootVal)
            self.pre_index+=1
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root

        return dfs(0, len(preorder)-1)