class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        map = defaultdict(list) #amount of characters from a-z -> word
        res = []

        for s in strs:
            characters = [0]*26
            for c in s:
                characters[ord(c)-ord('a')]+=1
            map[tuple(characters)].append(s)
        
        for key in map.keys():
            res.append(map[key])
        
        return res