class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)+1
        cols = len(text2)+1

        #Makes the entire dp table all 0's
        dp = [([0] * cols) for r in range(rows)]

        for r in range(rows-2,-1,-1):
            for c in range(cols-2,-1,-1):
                #1+diagonal, characters match
                if text1[r] == text2[c]:
                    dp[r][c] = 1+dp[r+1][c+1]
                #characters don't match, get max of bottom and right
                else:
                    dp[r][c] = max(dp[r][c+1], dp[r+1][c])

        return dp[0][0]