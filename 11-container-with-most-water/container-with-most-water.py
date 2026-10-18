class Solution:
    def maxArea(self, height: list[int]) -> int:
        if not height:
            return 0
        
        l = 0
        r = len(height)-1
        area = 0

        while l<r:
            area = max(area, (r-l)*(min(height[l],height[r])))
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return area