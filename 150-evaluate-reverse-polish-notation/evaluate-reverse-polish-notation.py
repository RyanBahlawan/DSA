class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for c in tokens:
            answer = 0
            if c == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                answer=val2+val1
                stack.append(answer)
            elif c == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                answer=val2-val1
                stack.append(answer)
            elif c == '*':
                val1 = stack.pop()
                val2 = stack.pop()
                answer=val2*val1
                stack.append(answer)
            elif c == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                answer=int(val2/val1)
                stack.append(answer)
            else:
                stack.append(int(c))
        return stack[0]