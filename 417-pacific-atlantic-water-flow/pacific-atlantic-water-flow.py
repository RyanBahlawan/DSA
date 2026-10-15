class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        self.rows = len(heights)
        self.cols = len(heights[0])

        def dfs(r,c,visit,prevHeight):
            #Base case we have already ran dfs on a point, out of bounds, or the previous height>current height
            if (r,c) in visit or r<0 or r>=self.rows or c<0 or c>=self.cols or heights[r][c]<prevHeight:
                return

            #Mark the point as visited which means we have never seen it before and previous height<=current height
            visit.add((r,c))
            #Run dfs N,E,S,W
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            return

        #Stores all the (r,c) visited
        pac = set()
        atl = set()

        #goes through the points where it already touches the water and runs dfs
        for c in range(self.cols):
            dfs(0,c,pac,heights[0][c])
            dfs(self.rows-1,c,atl,heights[self.rows-1][c])

        for r in range(self.rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,self.cols-1,atl,heights[r][self.cols-1])

        #Get the intersection between both sets
        res = []
        for r in range(self.rows):
            for c in range(self.cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res