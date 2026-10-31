class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        res = []
        subRes = []
        visit = set()

        def backtrack():
            if length == len(subRes):
                res.append(subRes.copy())
                return
            
            for n in nums:
                if n not in visit:
                    subRes.append(n)
                    visit.add(n)
                    backtrack()
                    subRes.pop()
                    visit.remove(n)
            return

        backtrack()
        return res