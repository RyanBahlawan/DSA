class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a>0:
                break
            
            if i>0 and nums[i-1] == nums[i]:
                continue
            
            l = i+1
            r = len(nums)-1
            while l<r:
                sum = a+nums[l]+nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
        return res