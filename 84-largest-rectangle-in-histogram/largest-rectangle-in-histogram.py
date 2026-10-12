class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] #[index, height]
        maxArea = 0

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                sI, sH = stack[-1]
                maxArea = max(maxArea, (i-sI)*(sH))
                start = sI
                stack.pop()
            stack.append([start,h])
        
        for i,h in stack:
            maxArea = max(maxArea, (len(heights)-i)*(h))

        return maxArea