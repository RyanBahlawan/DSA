class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxNum = 1
        minNum = 1
        res = max(nums)
        for n in nums:
            if n == 0:
                maxNum = 1
                minNum = 1
                continue

            temp = maxNum*n
            maxNum = max(maxNum*n,minNum*n,n)
            minNum = min(temp,minNum*n,n)
            res = max(res, maxNum)
        return res