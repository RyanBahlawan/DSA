class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        freq = defaultdict(int) #number -> count
        count = [[] for i in range(n+1)]
        res = []

        for num in nums:
            freq[num]+=1

        for key, val in freq.items():
            count[val].append(key)
        
        for i in range(n, -1, -1):
            for num in count[i]:
                if k!=0:
                    res.append(num)
                    k-=1
                else:
                    break

        return res