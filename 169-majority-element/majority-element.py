class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res = 0
        count = 0

        for i in range(len(nums)):
            if count == 0:
                res = nums[i]

            if res == nums[i]:
                count+=1
            else:
                count-=1
        return res