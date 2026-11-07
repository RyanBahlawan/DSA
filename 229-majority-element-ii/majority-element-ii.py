class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = defaultdict(int)
        minimum = len(nums)//3
        res = []

        for n in nums:
            if len(count)<2:
                count[n]+=1
                continue
            
            if n not in count:
                newCount = defaultdict(int)
                for key, val in count.items():
                    if val > 1:
                        newCount[key] = val-1
                count = newCount
            else:
                count[n]+=1
        for n in count:
            if nums.count(n)>minimum:
                res.append(n)
        return res