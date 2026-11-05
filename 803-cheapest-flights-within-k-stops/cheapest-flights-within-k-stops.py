class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        #index = airport, value = price to get to that airport
        prices = [float("infinity") for i in range(n)]

        #Starting airport cost nothing since we are starting there
        prices[src] = 0

        for i in range(k+1):
            #we have temp since it stores the current iteration results
            #This is because we compare with the previous iteration which is prices
            temp = prices.copy()
            for source, des, cost in flights:
                if prices[source] == float("infinity"):
                    continue
                if temp[des]>prices[source]+cost:
                    temp[des] = prices[source]+cost
            prices = temp
        
        if prices[dst] == float("infinity"):
            return -1
        else:
            return prices[dst]