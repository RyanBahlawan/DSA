class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s)+1)

        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                #Found a matching word
                if (i+len(w)<=len(s)) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]

                #If we made dp[i] True we get out of iterating through the word dictionary since we do not want to override it with a False
                if dp[i]:
                    break

        return dp[0]