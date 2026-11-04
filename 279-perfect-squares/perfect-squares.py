class Solution:
    def numSquares(self, n: int) -> int:
        #dp stores the best paths computed thus far
        dp = [n]*(n+1)
        dp[0] = 0

        #fill our cache from 1,n
        for i in range(1,n+1):
            #go through the squares from least to greatest until i<square
            for s in range(1, i+1):
                square = s**2
                if square>i:
                    break
                else:
                    index = i-square
                    dp[i] = min(dp[i], 1+dp[index])
        return dp[n]