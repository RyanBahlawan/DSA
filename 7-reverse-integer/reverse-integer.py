class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x<0:
            negative = True
            x*=-1

        MAX = (2**31) - 1
        MIN = 2**31

        res = 0

        while x:
            digit = x%10
            x=x//10

            if (not negative and res == MAX//10 and digit >=7) or (not negative and res>MAX//10):
                return 0

            if (negative and res == MIN//10 and digit >=8) or (negative and res>MIN//10):
                return 0

            res = (res*10)+digit
        
        if negative:
            res*=-1
        
        return res