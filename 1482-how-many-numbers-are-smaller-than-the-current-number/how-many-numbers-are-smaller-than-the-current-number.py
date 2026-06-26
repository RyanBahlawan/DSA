class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101 #make frequency list
        res = []

        for num in nums: #count
            count[num] = 1 + count[num]
        
        for i in range(1, 101): #prefix sum
            count[i] += count[i-1]
        
        for num in nums:
            if num == 0:
                res.append(0)
            else:
                res.append(count[num-1])
        
        return res
