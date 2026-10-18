class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        l = x
        count = 0

        while l:
            l = l//10
            count+=1

        l = 10**(count-1)
        
        while l>0:
            if x//l == x%10:
                x=x%l
                l=l//100
                x=x//10
            else:
                return False
        return True