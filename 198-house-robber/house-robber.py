class Solution:
    def rob(self, nums: list[int]) -> int:
        rob2 = 0
        rob1 = 0

        for n in nums:
            temp = max(rob1,rob2+n)
            rob2=rob1
            rob1 = temp
        return rob1