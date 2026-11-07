class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        i = 0

        #[-4,-1,-1,0,1,2]
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1

            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return res