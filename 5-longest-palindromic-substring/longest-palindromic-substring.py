class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        resLen = 0
        resIdx = 0
        for i in range(len(s)):
            #even
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l >= resLen:
                    resLen = max(resLen,r-l)
                    resIdx = l
                r+=1
                l-=1
            #odd
            l = i
            r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l >= resLen:
                    resLen = max(resLen,r-l)
                    resIdx = l
                r+=1
                l-=1
        return s[resIdx:resIdx+resLen+1]