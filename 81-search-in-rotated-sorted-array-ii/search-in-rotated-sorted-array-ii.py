class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2
            
            if nums[m] == target:
                return True
            
            #left portion
            elif nums[l]<nums[m]:
                if nums[l]<=target<nums[m]:
                    r=m-1
                else:
                    l = m+1
            #right portion
            elif nums[l]>nums[m]:
                if nums[m]<target<=nums[r]:
                    l = m+1
                else:
                    r=m-1
            #nums[l]==nums[m]
            else:
                l+=1
        return False