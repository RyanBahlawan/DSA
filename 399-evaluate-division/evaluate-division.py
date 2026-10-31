class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        #Build the adjacency list
        for i, eq in enumerate(equations):
            n1, n2 = eq
            adj[n1].append([n2,values[i]])
            adj[n2].append([n1,1/values[i]])

        def bfs(src, des):
            if src not in adj or des not in adj:
                return -1

            q = deque()
            visit = set()
            q.append([src, 1])
            visit.add(src)

            while q:
                length = len(q)
                for i in range(length):
                    node, curWeight = q.popleft()
                    if node == des:
                        return curWeight
                    for nei, weight in adj[node]:
                        if nei not in visit:
                            q.append([nei, curWeight*weight])
                            visit.add(nei)
            return -1


        res = []
        for src, des in queries:
            res.append(bfs(src, des))
        return res