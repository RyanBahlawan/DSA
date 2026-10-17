class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            #Check if we are in the left sorted portion
            if nums[l]<=nums[m]:
                #Move right pointer to the left portion
                if nums[l]<=target<nums[m]:
                    r = m-1
                #move left pointer to the right portion
                else:
                    l = m+1
            #Check if we are in the right sorted portion
            else:
                #Move left pointer to the right portion
                if nums[m]<target<=nums[r]:
                    l = m+1
                #move right pointer to the left portion
                else:
                    r = m-1

        return -1