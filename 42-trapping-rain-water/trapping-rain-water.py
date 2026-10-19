class Solution:
    def trap(self, height: list[int]) -> int:
        lMax = height[0]
        rMax=height[len(height)-1]
        res = 0
        
        l = 0
        r = len(height)-1

        while l<=r:
            if lMax<=rMax:
                lMax = max(lMax, height[l])
                res += (lMax-height[l])
                l+=1
            else:
                rMax = max(rMax, height[r])
                res += (rMax-height[r])
                r-=1

        return res