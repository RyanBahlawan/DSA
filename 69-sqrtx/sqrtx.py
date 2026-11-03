class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        prev = l

        while l<=r:
            m = (l+r)//2
            square = m*m
            if square == x:
                return m
            elif square > x:
                r=m-1
            elif square < x:
                l = m+1
                #This is the last greatest result before square goes over x
                prev = m
        
        #Returning the last greatest square that is less than x
        return prev