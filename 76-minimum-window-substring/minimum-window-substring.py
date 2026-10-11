class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        countS = {}

        for c in t:
            countT[c] = 1+countT.get(c,0)
        
        have = 0
        need = len(countT)
        l = 0
        r = 0
        resLen = float("infinity")
        res = [-1,-1]

        while r<len(s):
            countS[s[r]] = 1 + countS.get(s[r],0)
            if countS[s[r]] == countT.get(s[r],0):
                have+=1
            while have == need:
                if (r-l+1)<resLen:
                    resLen = r-l+1
                    res[0] = l
                    res[1] = r
                
                countS[s[l]]-=1
                if countS[s[l]] == (countT.get(s[l],0)) - 1:
                    have-=1
                l+=1
                
            r+=1

        if resLen != float("infinity"):
            return s[res[0]:res[1]+1]
        else:
            return ""