class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        #Solution set is between [1, len(nums)+1]
        n = len(nums)

        #make all number between (-00, 0] or [n+1, 00) to n+1 since they are not in the solution set
        for i in range(n):
            #Number is outside the solution set range
            if nums[i] <= 0 or nums[i]>n:
                nums[i] = n+1

        #mark numbers that exist as negative
        for i in range(n):
            index = abs(nums[i])-1
            if 0 <= index < n:
                if nums[index] > 0:
                    nums[index]*=-1

        #go through the solution set and check if it is in the array
        for j in range(1,n+1):
            if nums[j-1] > 0:
                return j

        return n+1