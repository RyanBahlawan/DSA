class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashset = set(nums)
        best = 0

        for n in hashset:
            length = 0
            if (n-1) not in hashset:
                while (n+length) in hashset:
                    length+=1
                best = max(length, best)
        return best