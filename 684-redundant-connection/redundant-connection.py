class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        #index->root; each index is the node and the value is the root
        parent = [i for i in range(n+1)]

        #rank is the size of the group based on the root(root is the leader)
        rank = [1]*(n+1)

        #finds the root
        def find(node):
            root = parent[node]

            #the root of the current node is not the same as the parent for the root node
            #Remember the root should be itself since it is the highest level
            while root!=parent[root]:
                #update the root to be the highest level by checking the grandparent
                parent[root] = parent[parent[root]]
                root = parent[root]
            return root

        #checks if there is a cycle, updates the rank, updates the parent list
        def union(n1,n2):
            #Get the roots of the nodes
            root1 = find(n1)
            root2 = find(n2)

            #cycle found
            if root1==root2:
                return False

            #Add root 2 into the bigger group
            if rank[root1]>rank[root2]:
                #make root 2 have the same root as root 1
                parent[root2] = parent[root1]
                rank[root1]+=rank[root2]
            #Add root 1 into the bigger group
            else:
                parent[root1] = parent[root2]
                rank[root2]+=rank[root1]
            return True


        for (n1,n2) in edges:
            if not union(n1,n2):
                return [n1,n2] 