class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers)-1

        while l<r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l+=1
            elif sum > target:
                r-=1
            else:
                return [l+1, r+1]