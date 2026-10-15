class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        #Build the prerequisite map
        self.preMap = {crs:[] for crs in range(numCourses)}
        for crs,pre in prerequisites:
            self.preMap[crs].append(pre)

        #Tracks DFS visited courses
        self.visit = set()

        #Goes Deep and checks base cases
        def dfs(crs):
            #No more neighbors
            if self.preMap[crs] == []:
                return True
            
            #We are in a cycle
            if crs in self.visit:
                return False

            #We have to check our neighbors
            self.visit.add(crs)
            for nei in self.preMap[crs]:
                if not dfs(nei):#We have seen a cycle
                    return False
            
            #We checked all of our neighbors
            self.visit.remove(crs)
            self.preMap[crs] = []
            return True
        
        #Goes through each vertice
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True