class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []

        #open and closed are the amount of brackets that are open and closed
        def backtrack(open, closed):
            #reached n for both
            if open==closed==n:
                res.append("".join(stack))
                return
            
            #we can add a ( bracket
            if open<n:
                stack.append("(")
                backtrack(open+1, closed)
                stack.pop()

            #We can add a ) bracket
            if closed<open:
                stack.append(")")
                backtrack(open, closed+1)
                stack.pop()
            return

        backtrack(0,0)
        return res