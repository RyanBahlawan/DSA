"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Dictionary maps the original nodes to the cloned nodes
        self.oldToNew = {}

        def dfs(node):
            if node in self.oldToNew: #we already made a clone
                return self.oldToNew[node]

            copy = Node(node.val)
            self.oldToNew[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy

        if not node:
            return None
        else:
            return dfs(node)