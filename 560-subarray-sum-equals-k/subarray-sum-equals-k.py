class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #The trick is (current Sum - previous Sum) = k
        #we store the prefix sum
        preSum = defaultdict(int) #prefixSum -> amount of times it occured so far
        preSum[0] = 1 #base case, previous sum of 0 occured once

        sum = 0
        res = 0
        for n in nums:
            sum+=n
            if (sum-k) in preSum:
                res+=preSum[sum-k]
            preSum[sum]+=1
        return res