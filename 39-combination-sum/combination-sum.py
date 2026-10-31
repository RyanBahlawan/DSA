class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        combinationSet = []

        #each decision we either include or exclude candidates[i]
        def dfs(i, sum):
            if i == len(candidates):
                return
            if sum>target:
                return
            if sum == target:
                res.append(combinationSet.copy())
                return
            
            #including candidates[i]
            combinationSet.append(candidates[i])
            sum+=candidates[i]
            dfs(i,sum)

            #excluding candidates[i]
            combinationSet.pop()
            sum-=candidates[i]
            dfs(i+1,sum)

        dfs(0,0)
        return res