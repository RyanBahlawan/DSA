class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n ==1:
            return [0]
        #Build the adjacency list
        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        #This is our queue
        leaves = deque()

        #Counts the amount of neighbours each node has
        countNei = {}

        for src, nei in adj.items():
            length = len(nei)
            #src is a leaf node
            if length == 1:
                leaves.append(src)
            
            #Maps the amount of neighbours a source node has
            countNei[src] = len(nei)

        #Run a bfs starting from the leaves and going towards the middle
        while leaves:
            #The remaining leaves are the minimum height trees
            if n<=2:
                return list(leaves)
            length = len(leaves)
            #Go through the level
            for i in range(length):
                #pop a leaf node (pretty muc removing it from the graph)
                node = leaves.popleft()
                n-=1
                #Go through the leafs neighbors
                for nei in adj[node]:
                    #decrement the neighbor count
                    countNei[nei]-=1
                    #Check if it became a leaf node
                    if countNei[nei] == 1:
                        #node has became a leaf node
                        leaves.append(nei)