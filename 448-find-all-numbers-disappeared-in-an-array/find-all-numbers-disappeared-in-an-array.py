class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])

        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        
        return res