class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0]*len(temperatures)
        stack = [] #[temperature, index]

        for i,t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                idx = stack[-1][1]
                res[idx] = i-idx
                stack.pop()
            stack.append([t,i])
        
        return res