class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        #build adjacency list
        adj = defaultdict(list) #src: [dist, des]
        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        minHeap = [] #stores [dist, point]
        heapq.heappush(minHeap, [0,0])
        visit = set()
        res = 0

        while minHeap:
            dist, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            
            visit.add(node)
            res+=dist

            for neiDist, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiDist, nei])
        return res