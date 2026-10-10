class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for j in range(len(nums)):
            diff = target - nums[j]

            if diff in seen:
                return [seen[diff], j]

            seen[nums[j]] = j

