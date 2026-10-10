class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for w in strs:
            chars = [0] * 26
            for c in w:
                chars[ord(c)-ord('a')] += 1
            anagrams[tuple(chars)].append(w)
        
        return list(anagrams.values())