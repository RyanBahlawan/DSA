class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        #Build adjacency list
        adj = defaultdict(list)

        for src, des, weight in times:
            adj[src].append((des, weight))
        
        minHeap = [] #stores (time, node)
        heapq.heappush(minHeap, (0, k))

        visit = set()
        res = 0

        while minHeap:
            #Gets the current time, and current node we are at
            time, curNode = heapq.heappop(minHeap)

            #We have already seen this node before, skip it
            if curNode in visit:
                continue

            #Add the node we are visiting
            visit.add(curNode)

            #update overall time
            res = max(res, time)
            
            #Add all of the adjacent nodes to the minHeap
            for des, weight in adj[curNode]:
                if des not in visit:
                    heapq.heappush(minHeap, (time+weight, des))

        #we have visited all nodes
        if len(visit)==n:
            return res
        #We have not visited all nodes
        else:
            return -1