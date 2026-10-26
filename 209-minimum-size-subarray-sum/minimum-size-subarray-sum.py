class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        sum = 0
        resLen = float("infinity")

        for r in range(len(nums)):
            sum += nums[r]
            if sum>=target:
                resLen = min(r-l+1, resLen)
                while sum>=target:
                    sum-=nums[l]
                    l+=1
                    if (r-l+1)<resLen and sum>=target:
                        resLen = r-l+1
        
        if resLen == float("infinity"):
            return 0
        else:
            return resLen