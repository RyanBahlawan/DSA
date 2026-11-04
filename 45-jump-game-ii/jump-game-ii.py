class Solution:
    def jump(self, nums: list[int]) -> int:
        res = 0
        l = 0
        r = 0

        while r<len(nums)-1:
            farthest = 0
            #go through the level
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            #Our window for the next level [l,r]
            l = r+1
            r = farthest
            res+=1
        return res