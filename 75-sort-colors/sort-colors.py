class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = 0 #everything before l is 0's
        r = len(nums)-1 #everything after r is 2's

        while i<=r:
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[l]
                nums[l] = temp
                l+=1
                i+=1
            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[r]
                nums[r] = temp
                r-=1
            else:
                i+=1
        return