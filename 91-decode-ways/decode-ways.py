class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp1 = 1
        dp2 = 1

        for i in range(1, len(s)):
            dp = 0
            #10 or 20
            if s[i] == '0' and s[i-1] in "12":
                dp = dp1
            
            #11<=n<=26
            elif (s[i] != '0' and s[i-1] in "1") or (s[i] in "0123456" and s[i-1] in "2"):
                dp = dp1+dp2

            #We encounter a 00 or number>27 but it has a zero meaning it must be 30,40,...
            elif s[i] == '0':
                return 0

            #current digit decodes by itself "single digit"
            else:
                dp = dp2

            dp1=dp2
            dp2 = dp
        

        return dp2