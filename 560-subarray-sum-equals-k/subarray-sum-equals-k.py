class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = {0:1}
        sum = 0
        res = 0

        for n in nums:
            sum +=n
            if (sum-k) in preSum:
                res+=preSum[sum-k]

            preSum[sum] = 1+preSum.get(sum,0)
        
        return res