class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [] #Stores the res
        subset = [] #Stores the subset
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
            return


        dfs(0)
        return res