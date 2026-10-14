# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #We will do preorder traversal and store it into a string
        self.res = []

        def dfs(node):
            if not node:
                self.res.append("N")
                return

            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(self.res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i = 0
        self.arr = data.split(",")

        def dfs():
            if self.arr[self.i] == "N":
                self.i+=1
                return None

            root = TreeNode(int(self.arr[self.i]))
            self.i+=1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))