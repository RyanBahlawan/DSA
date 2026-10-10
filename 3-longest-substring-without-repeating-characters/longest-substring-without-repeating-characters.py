class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = set()
        res = 0

        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l+=1
            count.add(s[r])

            res = max(r-l+1, res)
        
        return res