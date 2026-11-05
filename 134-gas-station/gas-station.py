class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        #cost is the amount of gas it takes to go from the ith station to the i+1 station
        #gas is the amount of gas our car gets filled up with

        #gas must be >= cost in order to make a loop
        if sum(gas)<sum(cost):
            return -1

        total = 0
        index = 0
        for i in range(len(gas)):
            #diff is the amount of gas we gain or lose to go to the next station
            diff = gas[i]-cost[i]

            #We cannot start at a negative diff station
            if total+diff<0:
                total=0 #reset total
                index=i+1 #try next position to be the starting position
            #We can move to the next gas station
            else:
                total+=diff
        return index