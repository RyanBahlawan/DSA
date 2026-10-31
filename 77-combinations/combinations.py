class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        currentCombination = []

        def brackTracking(start):
            #our combination has reached the size of k
            if len(currentCombination) == k:
                res.append(currentCombination.copy())
                return

            #Go from start to n; [start,n]
            for i in range(start, n+1):
                currentCombination.append(i)
                brackTracking(i+1)
                currentCombination.pop()
            return

        brackTracking(1)
        return res