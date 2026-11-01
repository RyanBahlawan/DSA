class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        res = []
        subRes = []

        nums.sort()

        def backtrack(i):
            if i == length:
                res.append(subRes.copy())
                return

            #Include nums[i]
            subRes.append(nums[i])
            backtrack(i+1)

            #Skip duplicates
            while i+1<length and nums[i]==nums[i+1]:
                i+=1

            #Exclude nums[i]
            subRes.pop()
            backtrack(i+1)

        backtrack(0)
        return res