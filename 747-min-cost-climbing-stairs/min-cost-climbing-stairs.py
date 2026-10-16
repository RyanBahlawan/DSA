class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        one = cost[len(cost)-2]
        two = cost[len(cost)-1]

        for i in range(len(cost)-3,-1,-1):
            temp = min(cost[i]+one, cost[i]+two)
            two = one
            one = temp

        return min(one,two)