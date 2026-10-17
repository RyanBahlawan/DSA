class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = float("infinity")
        while l<=r:
            k = (l+r)//2
            time = h
            for n in piles:
                amount =-(-n//k)
                time-=amount
                if time<0:
                    break

            if time >=0:
                res = min(res, k)
                r = k-1
            else:
                l = k+1
        
        return res