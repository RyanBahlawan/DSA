class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        length = sum(matchsticks)//4

        if sum(matchsticks)/4 != int(length):
            return False

        sides = [0]*4 #T,R,B,L
        matchsticks.sort(reverse=True)

        def backtrack(i):
            #Reached the end of the array
            if i == len(matchsticks):
                #check if all the sides are equal
                for j in range(4):
                    if length != sides[j]:
                        return False
                return True

            #goes through the 4 sides
            for j in range(4):
                #check if we can add that stick to that side
                if sides[j] + matchsticks[i]<=length:
                    sides[j]+=matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j]-=matchsticks[i]
            return False
        
        return backtrack(0)