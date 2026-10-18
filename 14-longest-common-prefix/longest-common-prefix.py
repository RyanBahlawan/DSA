class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        total = len(strs)-1
        end = 0
        res = []
        for i in range(len(strs[0])):
            count = 0
            for j in range(1,len(strs)):
                if i<=len(strs[j])-1 and strs[j][i] == strs[0][i]:
                    count +=1
            if total!=count:
                break
            else:
                end+=1
        
        return strs[0][:end]