class Solution:
    def checkValidString(self, s: str) -> bool:
        #leftMin is the minimum number of opening parenthesis that I need to close
        #leftMax is the maximum number of parenthesis that I need to close
        #the range of solutions is [leftMin, leftMax]
        leftMin = 0
        leftMax = 0

        for c in s:
            if c == '(':
                leftMin+=1
                leftMax+=1
            elif c == ')':
                leftMin-=1
                leftMax-=1
            #it is a '*'
            else:
                leftMin-=1 #treat '*' as a )
                leftMax+=1 #treat '*' as a (
            #leftMin cannot go lower than zero, that means that one of the * that we have seen must be an empty character
            if leftMin<0:
                leftMin = 0
            #we have closing parenthesis that cannot be closed since they're to the left
            if leftMax<0:
                return False
        
        #There is a way to close every single parenthesis
        if leftMin == 0:
            return True
        else:
            return False