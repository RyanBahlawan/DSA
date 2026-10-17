class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("infinity") for i in range(amount+1)]

        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a], 1+dp[a-c])

        if dp[amount] == float("infinity"):
            return -1
        else:
            return dp[amount]