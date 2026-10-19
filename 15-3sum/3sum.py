class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return []

        nums.sort()
        res=[]

        for i in range(len(nums)):
            a=nums[i]

            if a>0:
                break
            
            if i>0 and nums[i]==nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1
            while l<r:
                b = nums[l]
                c = nums[r]
                if a+b+c == 0:
                    res.append([a,b,c])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif a+b+c<0:
                    l+=1
                else:
                    r-=1
                

        return res            