class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {']':'[', '}':'{', ')':'('}

        for c in s:
            if c in map:
                if stack and map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False