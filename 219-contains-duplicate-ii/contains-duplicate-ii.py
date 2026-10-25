class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        l = 0
        window = set()

        for r in range(len(nums)):
            while (r-l)>k:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False