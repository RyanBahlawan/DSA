class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        #A town where there is only 1 person and they trust nobody
        if len(trust) == 0 and n==1:
            return n

        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        #go through the entire trust list and store the amount of outgoing and incoming for each node
        for (source,destination) in trust:
            incoming[destination]+=1
            outgoing[source]+=1

        #Go through the incoming hashmap
        for (townJudge, amount) in incoming.items():
            #Check if it is a town judge
            #A town judge has everyone trusting him (n-1) and he dowsn't trust anyone (0)
            if amount == n-1 and outgoing[townJudge] == 0:
                return townJudge

        return -1