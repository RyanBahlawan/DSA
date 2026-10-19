class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {']':'[','}':'{',')':'('}
        stack = []

        for c in s:
            #Closed
            if c in closedToOpen:
                #Matching open and closed
                if stack and closedToOpen[c]==stack[-1]:
                    stack.pop()
                
                #not matching
                else:
                    return False
            
            #Open
            else:
                stack.append(c)

        if stack:
            return False
        else:
            return True
