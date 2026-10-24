class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = 0 #defines the left portion is 0
        r = len(nums)-1 #defines the right portion is 2

        while i<=r:
            if nums[i]==0:
                temp = nums[i]
                nums[i] = nums[l]
                nums[l] = temp
                l+=1
            elif nums[i]==2:#we don't increment i for when nums[i]==2
                temp = nums[i]
                nums[i] = nums[r]
                nums[r] = temp
                r-=1
                i-=1
            i+=1
        
        return