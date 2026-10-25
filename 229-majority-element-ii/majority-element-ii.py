class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = defaultdict(int)
        res = []
        minimum = len(nums)//3

        for n in nums:
            count[n]+=1
            if len(count)<=2:
                continue
            
            new_count = defaultdict(int)
            for k,v in count.items():
                if v>1:
                    new_count[k] = v-1
            
            count = new_count

        for n in count:
            if nums.count(n) > minimum:
                res.append(n)

        return res