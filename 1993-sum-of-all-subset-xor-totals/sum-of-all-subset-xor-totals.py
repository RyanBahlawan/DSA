class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        #Sum of subset XORs = (OR of all numbers) x (2^n-1)
        res = 0
        for n in nums:
            res |= n
        
        return res*(2**(len(nums)-1))