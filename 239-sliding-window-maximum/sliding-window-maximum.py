class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = deque() #indices
        l=0
        r=0

        while r<len(nums):
            #remove the numbers that are < the numbers to the right
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #Remove number that are not in the window
            if q and l > q[0]:
                q.popleft()

            #Checks if we have our window size of at least k
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            
            r+=1

        return output