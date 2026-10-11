class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height)-1
        lMax = height[l]
        rMax = height[r]
        total = 0

        while l<r:
            if lMax<=rMax:
                l+=1
                lMax = max(lMax, height[l])
                total += lMax-height[l]
            else:
                r-=1
                rMax = max(rMax, height[r])
                total += rMax-height[r]
        return total