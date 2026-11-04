class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums)-1 #the goal is the location where we are trying to get to
        length = 1 #distance from i to the goal
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i]>=length:
                length = 1
                goal = i
            else:
                length +=1

        if goal == 0:
            return True
        else:
            return False