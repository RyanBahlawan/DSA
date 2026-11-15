class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(num):
            sum = 0

            while num:
                digit = num%10
                sum+=(digit**2)
                num = num//10
            
            return sum

        visit = set()

        while n not in visit:
            if n==1:
                return True
            
            visit.add(n)
            n = sumOfSquares(n)
        return False