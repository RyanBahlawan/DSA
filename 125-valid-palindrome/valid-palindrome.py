class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l<r:
            if not self.isAlphanum(s[l]):
                l+=1
            elif not self.isAlphanum(s[r]):
                r-=1
            elif s[l].lower() == s[r].lower():
                r-=1
                l+=1
            else:
                return False
        return True

    def isAlphanum(self, c):
        if (ord('a')<=ord(c)<=ord('z') or ord('A')<=ord(c)<=ord('Z') or ord('0')<=ord(c)<=ord('9')):
            return True
        else:
            return False