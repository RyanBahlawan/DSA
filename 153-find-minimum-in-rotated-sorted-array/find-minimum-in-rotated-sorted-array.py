class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]

        while l<=r:
            #we are in ascending order
            if nums[l]<nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r)//2
            res = min(res, nums[m])
            #search right
            if nums[l]<=nums[m]:
                l = m+1
            #search left
            else:
                r=m-1

        return res