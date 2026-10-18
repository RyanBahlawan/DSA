class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        total = len(strs)-1
        res = []
        for i in range(len(strs[0])):
            count = 0
            for w in strs[1:]:
                if i<=len(w)-1 and w[i] == strs[0][i]:
                    count +=1
            if total!=count:
                break
            else:
                res.append(strs[0][i])
        
        return "".join(res)