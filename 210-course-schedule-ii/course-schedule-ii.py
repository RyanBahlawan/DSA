class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        #Build the adjacency list
        self.adj = {c:[] for c in range(numCourses)}
        for c,p in prerequisites:
            self.adj[c].append(p)

        #Keeps track of what the dfs has visited
        self.visit = set()
        #Keeps track of what we added to the res
        self.inRes = set()

        self.res = []

        def dfs(course):
            #cycle detected
            if course in self.visit:
                return False

            #Already seen the course before
            if course in self.inRes:
                return True

            #Base case
            if self.adj[course] == []:
                self.res.append(course)
                self.inRes.add(course)
                return True

            self.visit.add(course)
            for nei in self.adj[course]:
                if not dfs(nei):
                    return False

            #Visited all neighbors
            self.adj[course] = []
            self.visit.remove(course)
            self.res.append(course)
            self.inRes.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return self.res