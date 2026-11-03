class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        #Since it is on a conveyer belt, the input array cannot be sorted.
        #We want to minimize the capacity that we want to put onto the ship
        #We know that capacity range is between [max(weights), sum(weights)]
        #We will do a binary search on this capacity range

        #returns whether we can load each ship with capacity with days
        def minCap(capacity):
            amountOfDays = 1 #since we are loading the first ship on the first day
            curCapacity = 0 #current capacity of the ship
            i = 0
            #iterate through the array
            while i<len(weights):
                #cannot fill the ships within the designated days
                if amountOfDays>days:
                    return False
                #we can fill the ship
                elif curCapacity+weights[i]<=capacity:
                    curCapacity+=weights[i]
                #ship cannot be filled anymore, go to the next day
                else:
                    amountOfDays+=1
                    curCapacity = 0
                    i-=1
                i+=1
            #we can fill all ships
            return True

        l = max(weights) #minimum a boat can carray
        r = sum(weights) #maximum a boat can carry
        res = r #initialize it as the maximum

        while l<=r:
            m = (l+r)//2
            if minCap(m):
                res = min(res, m)
                r=m-1
            else:
                l=m+1
            
        return res