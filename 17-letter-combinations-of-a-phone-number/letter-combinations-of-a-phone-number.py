class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        part = []
        numToChar = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        def backtrack(i):
            #we mapped an instance
            if len(part)==len(digits):
                res.append("".join(part))
                return

            #each level we go through each character
            for c in numToChar[digits[i]]:
                part.append(c)
                backtrack(i+1)
                part.pop()

        if digits:
            backtrack(0)
        return res