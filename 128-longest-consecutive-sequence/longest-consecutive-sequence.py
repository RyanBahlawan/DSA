class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashset = set(nums)
        best = 0

        for n in hashset:
            #start of the sequence
            if not(n-1 in hashset):
                i = 0
                res = 0
                while n+i in hashset:
                    res+=1
                    i+=1
                best = max(res,best)

        return best