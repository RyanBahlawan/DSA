class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] not in char:
                char.add(s[r])
            else:
                while s[r] in char:
                    char.remove(s[l])
                    l+=1
                char.add(s[r])
            res = max(r-l+1,res)
        
        return res