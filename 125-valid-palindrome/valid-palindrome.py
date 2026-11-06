class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isValid(c):
            if ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9') or ord('A')<=ord(c)<=ord('Z'):
                return True
            else:
                return False
    
        l = 0
        r = len(s)-1

        while l<r:
            if not isValid(s[l]):
                l+=1
            elif not isValid(s[r]):
                r-=1
            else:
                if s[l].lower()==s[r].lower():
                    l+=1
                    r-=1
                else:
                    return False
        return True