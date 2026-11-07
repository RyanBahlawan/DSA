class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height)-1
        
        lMax = height[l]
        rMax = height[r]
        total = 0

        while l<=r:
            if lMax<=rMax:
                lMax = max(lMax, height[l])
                total+=lMax-height[l]
                l+=1
            else:
                rMax = max(rMax, height[r])
                total+=rMax-height[r]
                r-=1
        return total