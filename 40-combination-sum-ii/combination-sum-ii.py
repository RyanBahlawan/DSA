class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        combinationSet = []

        candidates.sort()

        def dfs(i, sum):
            if sum == target:
                res.append(combinationSet.copy())
                return
            if i == len(candidates):
                return
            if sum>target:
                return
            

            #include candidates[i]
            combinationSet.append(candidates[i])
            sum+=candidates[i]
            dfs(i+1,sum)

            #exclude candidates[i]
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            combinationSet.pop()
            sum-=candidates[i]
            dfs(i+1,sum)

            return

        dfs(0,0)
        return res