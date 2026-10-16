class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resIdx = 0

        for i in range(len(s)):
            #odd
            l = i
            r = i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)>resLen:
                    resLen = r-l+1
                    resIdx = l
                r+=1
                l-=1
                
            #Even
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)>resLen:
                    resLen = r-l+1
                    resIdx = l
                r+=1
                l-=1

        return s[resIdx:resIdx+resLen]