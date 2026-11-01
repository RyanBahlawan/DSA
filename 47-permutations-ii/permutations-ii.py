class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        res = []
        subRes = []
        count = defaultdict(int)

        for n in nums:
            count[n]+=1

        def backtrack():
            if length == len(subRes):
                res.append(subRes.copy())
                return
            
            for n in count:
                if count[n]>0:
                    subRes.append(n)
                    count[n]-=1
                    backtrack()
                    count[n]+=1
                    subRes.pop()
            return

        backtrack()
        return res