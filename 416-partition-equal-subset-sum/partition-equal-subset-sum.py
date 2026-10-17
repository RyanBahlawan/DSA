class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        target = total//2

        if total % 2 != 0:
            return False

        sums = set([0])

        for i in range(len(nums)-1,-1,-1):
            newSums = set()
            for num in sums:
                newSums.add(nums[i]+num)
                newSums.add(num)

            sums = newSums

            if target in sums:
                return True

        if target in sums:
            return True
        else:
            return False