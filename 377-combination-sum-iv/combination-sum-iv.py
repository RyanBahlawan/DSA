class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        #dp[x] means how many combinations from nums can add up to x
        dp = [0]*(target+1)
        dp[0] = 1

        #we fill our cache from 1,n
        #go from 1,n and we ask how many ways can I go to i from my nums
        for i in range(1,target+1):
            for n in nums:
                index = i-n
                if index>=0:
                    dp[i] += dp[index]
        return dp[target]