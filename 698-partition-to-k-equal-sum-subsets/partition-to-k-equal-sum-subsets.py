class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums)//k

        if target != sum(nums)/k:
            return False

        used = [False]*len(nums)
        nums.sort(reverse=True)

        if nums[0]>target:
            return False

        def backtrack(i, k, curSum):
            #filled a subset
            if target == curSum:
                return backtrack(0,k-1,0)
            
            #Found all possible partitions
            if k == 0:
                return True

            #Go through all the numbers
            for j in range(i,len(nums)):
                if used[j] or curSum+nums[j]>target:
                    continue
                if not used[j] and curSum+nums[j]<=target:
                    curSum+=nums[j]
                    used[j] = True
                    if backtrack(j+1, k, curSum):
                        return True
                    used[j] = False
                    curSum-=nums[j]
            return False


        return backtrack(0, k, 0)