class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(largest):
            curSum = 0
            groups = 1

            for n in nums:
                if curSum+n<=largest:
                    curSum+=n
                else:
                    curSum = n
                    groups+=1
            
            if groups<=k:
                return True
            else:
                return False

        #we are running a binary search from [largest num in nums, sum of nums]
        l = max(nums)
        r = sum(nums)
        res = r

        while l<=r:
            mid = (l+r)//2

            #we can split this sum into k groups
            if canSplit(mid):
                res = mid
                r=mid-1
            #we cannot split this sum into k groups
            else:
                l = mid+1
        return res