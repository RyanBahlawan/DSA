class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key,val in count.items():
            freq[val].append(key)

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res